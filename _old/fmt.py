b = 'Consolidated Condensed Statements of Income - USD ($) shares in Thousands, $ in Millions'

c = 'Consolidated Statements of Operations - USD ($) $ in Millions'

d = 'Consolidated Statements of Operations - USD ($) shares in Millions'

header = b.lower().replace(' ', '')
unitinfo = header[header.find('usd($)')+6:]

iscurrencymod = 1
sharemod = 1
bscurrencymod = 1
print(unitinfo)
if '$' in unitinfo:
    unit = unitinfo[unitinfo.find('$'):][0:10]
    print(unit)
    if 'million' in unit:
        iscurrencymod = 1000000
    elif 'thousand' in unit:
        iscurrencymod = 1000

if 'shares' in unitinfo:
    unit = unitinfo[unitinfo.find('shares')+6:][0:10]
    print(unit)

    if 'million' in unit:
        sharemod = 1000000
    elif 'thousand' in unit:
        sharemod = 1000


b = 'Consolidated Statements of Operations - USD ($) $ in Millions'
header = b.lower().replace(' ', '')
unitinfo = header[header.find('usd($)')+6:]

if '$' in unitinfo:
    unit = unitinfo[unitinfo.find('$')+1:][0:10]
    print(unit)

    if 'million' in unit:
        bscurrencymod = 1000000
    elif 'thousand' in unit:
        bscurrencymod = 1000

print(iscurrencymod, sharemod, bscurrencymod)

# print(unitinfo)



# bslongtext = {

# }

# lookups = {
#     # '': 'NA',
#     # 'nan': 'NAN',
#     # 'none': 'NONE',b = 'Consolidated Condensed Statements of Income - USD ($) shares in Millions, $ in Millions'

#     'netrevenue': 'NR',
#     'revenues': 'NR',
#     'totalrevenue': 'NR',
#     'netsales': 'NR',

#     'costofsales': 'COGS',
#     'merchandisecosts': 'COGS',
#     'costofgoodssold': 'COGS',

#     'marketinggeneralandadministrative': 'SGA',
#     'sellinginformationalandadministrativeexpenses': 'SGA',
#     'sellinggeneralandadministrative': 'SGA',
#     'sellinggeneralandadministrativeexpenses': 'SGA',

#     'researchanddevelopment': 'RND',
#     'researchanddevelopmentexpenses': 'RND',
#     'researchanddevelopmentexpense': 'RND',
#     'researchanddevelopmentcosts': 'RND',

#     'netincome': 'NI',
#     'netincomeattributabletocompany': 'NI',
#     'netearnings': 'NI',

#     'dilutedshares': 'SHARES',
#     'weightedaveragesharesdiluted': 'SHARES',
#     'dilutedshares': 'SHARES',
#     'diluted': 'SHARES',
# }

# bslookups = {

#     'cashandcashequivalents': 'CCE',

#     'accountsreceivable': 'AR',
#     'receivablesnet': 'AR',
#     'accountsandnotesreceivablenet': 'AR',

#     'inventories': 'IN',
#     'merchandiseinventories': 'IN',

#     'totalcurrentassets': 'TCA',
#     'totalassets': 'TA',

# }

# fuzzylookups = {

#     'cashandcashequivalents': 'cashandcashequivalents',
#     'accountsreceivable': 'accountsreceivable',
#     'netincomeattributableto': 'netincomeattributabletocompany',
# }

# avoid = { # values from fuzzylookups
#     'netincomeattributabletocompany': ['less', 'share', 'stock']

# }

# def check(r):
#     r = str(r).lower()
#     replace_chars = [',', '(', ')', '.', '-', '???', ' ']
#     for c in replace_chars:
#         r = r.replace(c, '')
#     if r in lookups.keys():
#         return r
#     else:
#         for fzy in fuzzylookups.keys():
#             if fzy in r:
#                 if fuzzylookups[fzy] in avoid.keys():
#                     for a in avoid[fuzzylookups[fzy]]:
#                         if a in r:
#                             return -1
#                     return fuzzylookups[fzy]

#         return -1
        

#     # if r in lookups.keys():
#     #     return r # longtext[lookups[r]]
#     # else:
#     #     return -1

#     # print(f)
#     # print(longtext[lookups[f]])
#     # print(bslongtext[bslookups[f]])


# import pandas as pd

# df = pd.read_excel('C:/Users/djg286/OneDrive - Corteva/Desktop/down/sample.xlsx', sheet_name='Sheet1')
# rowheaders = list(df[df.columns[0]])

# search = list(df[df.columns[1]])
# col_name = df.columns[1]
# for c in search:
#     c = str(c)
#     if '[' in c or ']' in c:
#         col_name = df.columns[2]
#         break

# col = col_name.lower()
# if '3' in col and 'month' in col:
#     period_type = '3-month'
# elif '12' in col and 'month' in col:
#     period_type = '12-month'
# else:
#     period_type = 'unknown'

# print(period_type)

# period_ended = df.loc[0, col]
# print(period_ended)

# # for r in rowheaders:
# #     field = check(r)
# #     if field != -1:
# #         # print(r)
# #         print(lookups[field])


# # r = 'Weighted-average shares??????diluted'
# # print(check(r))