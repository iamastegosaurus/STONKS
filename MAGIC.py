import pandas as pd
import os 

from parse_helpers.get_date import get_date
from parse_helpers.get_sheet_names import get_sheet_names
from parse_helpers.get_lookups import get_lookups
from parse_helpers.get_longtext import get_longtext


longtext, iscount = get_longtext()

path = 'Q:/STONKS/downloads/'

# TODO: add eps to pull for when they don't put sharecount, just eps

ticker = 'TXN'
overallnumbermod = 1000000

path = path + ticker
filings = [f for f in os.listdir(path) if '_10-' in f and '~$' not in f]

data = []
labels = ['filing_date', 'filing_type', 'period_type', 'period_ended']
for l in longtext.keys():
    labels.append(l)

for file in filings:
    print(file)
    # file = filings[0]
    f = file.split('.')[0]

    filepath = path + '/' + file
    filing_date = f.split('_')[0]
    filing_type = f.split('_')[1]

    # ALL INCOME STATEMENT ONLY
    income_sheet_name, balance_sheet_name, iscurrencymod, sharemod, bscurrencymod = get_sheet_names(filepath)
    df = pd.read_excel(filepath, sheet_name = income_sheet_name)

    newest_year = 2000
    newest_month = 1
    newest_date = ''

    period_type = ''
    for col in list(df.columns)[1:]:
        c = col.lower()
        if '3' in c and 'month' in c:
            period_type = '3-month'
        elif '12' in c and 'month' in c:
            period_type = '12-month'
        elif 'unnamed' in c:
            pass
        elif 'month' in c:
            pass
        else:
            period_type = 'unknown'

        if period_type == '3-month' or period_type == '12-month':

            if str(df.loc[0, col]) != 'nan':
                period_date = get_date(df.loc[0, col])

                period_year = int(period_date.split('-')[0])
                period_month = int(period_date.split('-')[1])

                if period_year > newest_year:
                    col_name = col
                    newest_month = period_month
                    newest_year = period_year
                    newest_date = period_date

                elif period_month > newest_month and period_year == newest_year:
                    col_name = col
                    newest_month = period_month
                    newest_date = period_date
                    
    period_date = newest_date

    rowheaders = list(df[df.columns[0]])
    fieldmap = {}
    datamap = {}

    shareonlynow = False

    for row in rowheaders:
        field = get_lookups(row)
        if field != -1:
            if shareonlynow == False:
                fieldmap[field] = row
                if field == 'SHARES':
                    shareonlynow = True
            else:
                if field == 'SHARES':
                    fieldmap[field] = row

    for field in list(longtext.keys()):
        if field in fieldmap.keys():
            datamap[field] = df.loc[df[df.columns[0]] == fieldmap[field]][col_name].values[0] * iscurrencymod / overallnumbermod # had values[0] previously, may need more logic if multiple match
        else:
            datamap[field] = ''

    if datamap['SHARES'] != '':
        datamap['SHARES'] = datamap['SHARES'] * (sharemod / iscurrencymod)

    line = [filing_date, filing_type, period_type, period_date]

    # print(datamap)
    # BALANCE SHEET TIME
    df = pd.read_excel(filepath, sheet_name = balance_sheet_name)
    
    if 'unnamed' in str(df.columns[1]).lower():
        col_name = df.columns[2]
    else:
        col_name = df.columns[1]

    rowheaders = list(df[df.columns[0]])
    for row in rowheaders:
        field = get_lookups(row)
        if field != -1:
            fieldmap[field] = row

    for field in list(longtext.keys())[iscount:]:
        if field in fieldmap.keys():
            datamap[field] = df.loc[df[df.columns[0]] == fieldmap[field]][col_name].values[0] * bscurrencymod / overallnumbermod 
        else:
            datamap[field] = ''


    for d in datamap.keys():
        line.append(datamap[d])

    data.append(line)


res = pd.DataFrame(data, columns = labels)
try:
    res.to_excel(path + '/auto.xlsx', index=False)
except Exception as e:
    if '[Errno 13] Permission denied:' in str(e):
        res.to_excel(path + '/CLOSE THE FILE IDIOT.xlsx', index=False)
    else:
        print(e)
