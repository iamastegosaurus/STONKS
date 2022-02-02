import os
import pandas as pd

def create_template(path, ticker):

    path = path + ticker
    if os.path.isfile(path + '\\aggregate.xlsx'):
        print('exists')
        return
    else:
        filings = os.listdir(path)
        filenames = [f.split('.')[0] for f in filings if '_10-' in f]

        dates = [f.split('_')[0] for f in filenames]
        types = [f.split('_')[1] for f in filenames]

        a = [ [dates[i], types[i], '', '', '', '', '', '', '', '', '', ''] for i in range(len(dates))]
        
        df = pd.DataFrame(a, columns=[
            'date', 
            'filing_type', 
            'revenue', 
            'expenses', 
            'net_income', 
            'shares', 
            'current_assets', 
            'total_assets', 
            'current_liabilities', 
            'longterm_debt', 
            'total_liabilities', 
            'shareholder_equity'
            ])

        df.to_excel(path + '\\aggregate.xlsx', index=False)