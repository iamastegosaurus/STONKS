import os
import pandas as pd

tickers = ['RTX']

for ticker in tickers:

    dates = []
    shares = []
    netincome = []
    shareholderequity = []

    path = 'Q://STONKS//downloads//' + ticker
    filings = os.listdir(path)[::-1]
    filings = [f for f in filings if f.split('.')[1] == 'xlsx' and '$' not in f and 'combined' not in f]
    k_indexes = [i for i, f in enumerate(filings) if 'K' in f]
    
    lastk = k_indexes[-1]
    if lastk > len(filings) - 3:
        filings = filings[:lastk]
        k_indexes = k_indexes[:-1]
    
    for findex, f in enumerate(filings):
        dates.append(f.split('_')[0])
        income_statement = pd.read_excel(path + '//' + f, sheet_name='IncomeStatement')
        balance_sheet = pd.read_excel(path + '//' + f, sheet_name='BalanceSheet')
        income_rows = list(income_statement['words'])
        balance_rows = list(balance_sheet['words'])

        if findex in k_indexes:
            netincome.append('circleback')
        else:
            for item in income_rows[::-1]: 
                i = str(item).lower()
                if 'net' in i and ('income' in i or 'earnings' in i or 'loss' in i) and 'shares' not in i:
                    nis = income_statement.loc[income_statement['words'] == item]['3-month'].values
                    for n in nis:
                        if '.' not in str(n):
                            ni = n
                    if ni > abs(1000000):
                        ni = ni / 1000000
                    netincome.append(ni)
                    break

        for item in income_rows[::-1]: 
            i = str(item).lower()
            if 'diluted' in i or ('denom' in i and 'earnings' in i):
                try:
                    sh = income_statement.loc[income_statement['words'] == item]['3-month'].values[-1]   #item())
                except:
                    sh = income_statement.loc[income_statement['words'] == item][income_statement.columns[1]].values[-1]   #.item()
                shares.append(sh)
                break
        # IF CAN'T FIND SHARE COUNT, JUST USE FROM THE 10-K

        for item in balance_rows[::-1]: 
            i = str(item).lower()
            if 'total' in i and 'equity' in i and 'liabilities' not in i:
                shareholderequity.append(balance_sheet.loc[balance_sheet['words'] == item][balance_sheet.columns[1]].item())
                break

    for k in k_indexes:
        f = filings[k]
        income_statement = pd.read_excel(path + '//' + f, sheet_name='IncomeStatement')
        income_rows = list(income_statement['words'])

        for item in income_rows[::-1]: 
            i = str(item).lower()
            if 'net' in i and ('income' in i or 'earnings' in i or 'loss' in i) and 'shares' not in i:
                year_incomes = income_statement.loc[income_statement['words'] == item][income_statement.columns[1]].values
                for y in year_incomes:
                    if '.' not in str(y):
                        year_income = y

                if year_income > abs(1000000):
                    year_income = year_income / 1000000
                break

        q3 = netincome[k + 1]
        q2 = netincome[k + 2]
        q1 = netincome[k + 3]

        q4 = year_income - q3 - q2 - q1
        netincome[k] = q4

    eps = [netincome[i] / shares[i] for i in range(len(netincome))]
    bvps = [shareholderequity[i] / shares[i] for i in range(len(netincome))]

    df = pd.DataFrame(list(zip(
        dates,
        eps,
        bvps,
        netincome,
        shareholderequity,
        shares
    )), columns=['DATE', 'EPS', 'BVPS', 'NETINCOME', 'BV', 'SHARECT'])
    df.to_csv('Q://STONKS//downloads//' + ticker + '//' + 'financials.csv', index=False)

# income statment:
# find 'diluted' and 'shares'

# find either:
# net income or earnings per share


# balance sheet:
# find 'total' and 'equity' without 'liabilities'