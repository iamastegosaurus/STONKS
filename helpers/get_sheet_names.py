import pandas as pd

def get_sheet_names(filepath):
    sheet_names = pd.ExcelFile(filepath, engine = 'openpyxl').sheet_names

    for s in sheet_names[0:7]:
        sheet = pd.read_excel(filepath, sheet_name = s)
        header = sheet.columns[0].lower().replace(' ', '')

        # if ('income' in header or 'operations' in header or 'earnings' in header) and (('comprehensive' not in header and 'parenthetical' not in header) or ('andcomprehensive' in header)): 

        if ('income' in header or 'operations' in header or 'earnings' in header) and ('comprehensive' not in header and 'parenthetical' not in header): 
            income_sheet_name = s
            isheader = header
        elif ('balance' in header) and ('parenthetical' not in header):
            balance_sheet_name = s
            bsheader = header
        else:
            pass

    unitinfo = isheader[isheader.find('usd($)')+6:]

    iscurrencymod = 1
    sharemod = 1
    bscurrencymod = 1

    if '$' in unitinfo:
        unit = unitinfo[unitinfo.find('$'):][0:10]

        if 'million' in unit:
            iscurrencymod = 1000000
        elif 'thousand' in unit:
            iscurrencymod = 1000

    if 'shares' in unitinfo:
        unit = unitinfo[unitinfo.find('shares')+6:][0:10]

        if 'million' in unit:
            sharemod = 1000000
        elif 'thousand' in unit:
            sharemod = 1000

    unitinfo = bsheader[bsheader.find('usd($)')+6:]

    if '$' in unitinfo:
        unit = unitinfo[unitinfo.find('$')+1:][0:10]

        if 'million' in unit:
            bscurrencymod = 1000000
        elif 'thousand' in unit:
            bscurrencymod = 1000
    
    return income_sheet_name, balance_sheet_name, iscurrencymod, sharemod, bscurrencymod
