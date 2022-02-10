b = 'Consolidated Condensed Statements of Income - USD ($) shares in Millions, $ in Millions'
b = b.lower().replace(' ', '')

usd = b.find('usd($)')

unitinfo = b[usd+6:]

# print(unitinfo)

longtext = {
    'NA': 'Field not present', # probably unnecessary
    'NAN': '',
    'NONE': '',

    'NR': 'Net revenue',
    'COGS': 'Cost of goods sold',
    'SGA': 'Selling, general, and administrative',
    'RND': 'Research and development',

    'NI': 'Net income',
    'SHARES': 'Diluted common shares outstanding'

}

bslongtext = {
    'CCE': 'Cash and cash equivalents',
    'AR': 'Accounts receivable',
    'IN': 'Inventories',
    'TCA': 'Total current assets',
    'TA': 'Total assets'
}

lookups = {
    # '': 'NA',
    # 'nan': 'NAN',
    # 'none': 'NONE',

    'netrevenue': 'NR',
    'revenues': 'NR',
    'totalrevenue': 'NR',
    'netsales': 'NR',

    'costofsales': 'COGS',
    'merchandisecosts': 'COGS',
    'costofgoodssold': 'COGS',

    'marketinggeneralandadministrative': 'SGA',
    'sellinginformationalandadministrativeexpenses': 'SGA',
    'sellinggeneralandadministrative': 'SGA',
    'sellinggeneralandadministrativeexpenses': 'SGA',

    'researchanddevelopment': 'RND',
    'researchanddevelopmentexpenses': 'RND',
    'researchanddevelopmentexpense': 'RND',
    'researchanddevelopmentcosts': 'RND',

    'netincome': 'NI',
    'netincomeattributabletocompany': 'NI',
    'netearnings': 'NI',

    'dilutedshares': 'SHARES',
    'weightedaveragesharesdiluted': 'SHARES',
    'dilutedshares': 'SHARES',
    'diluted': 'SHARES',


}

bslookups = {

    'cashandcashequivalents': 'CCE',

    'accountsreceivable': 'AR',
    'receivablesnet': 'AR',
    'accountsandnotesreceivablenet': 'AR',

    'inventories': 'IN',
    'merchandiseinventories': 'IN',

    'totalcurrentassets': 'TCA',
    'totalassets': 'TA',

}

fuzzylookups = {

    'cashandcashequivalents': 'cashandcashequivalents',
    'accountsreceivable': 'accountsreceivable',
    'netincomeattributableto': 'netincomeattributabletocompany',
}

avoid = { # values from fuzzylookups
    'netincomeattributabletocompany': ['less', 'share', 'stock']

}

def check(r):
    r = str(r).lower()
    replace_chars = [',', '(', ')', '.', '-', '–', ' ']
    for c in replace_chars:
        r = r.replace(c, '')
    if r in lookups.keys():
        return r
    else:
        for fzy in fuzzylookups.keys():
            if fzy in r:
                if fuzzylookups[fzy] in avoid.keys():
                    for a in avoid[fuzzylookups[fzy]]:
                        if a in r:
                            return -1
                    return fuzzylookups[fzy]

        return -1
        

    # if r in lookups.keys():
    #     return r # longtext[lookups[r]]
    # else:
    #     return -1

    # print(f)
    # print(longtext[lookups[f]])
    # print(bslongtext[bslookups[f]])


import pandas as pd

df = pd.read_excel('C:/Users/djg286/OneDrive - Corteva/Desktop/down/sample.xlsx', sheet_name='Sheet1')
rowheaders = list(df[df.columns[0]])

search = list(df[df.columns[1]])
col = df.columns[1].lower()
for c in search:
    c = str(c)
    if '[' in c or ']' in c:
        col = df.columns[2].lower()
        break

if '3' in col and 'month' in col:
    period_type = '3-month'
elif '12' in col and 'month' in col:
    period_type = '12-month'
else:
    period_type = 'unknown'

print(period_type)

period_ended = df.loc[0, col]
print(period_ended)

# for r in rowheaders:
#     field = check(r)
#     if field != -1:
#         # print(r)
#         print(lookups[field])


# r = 'Weighted-average shares––diluted'
# print(check(r))