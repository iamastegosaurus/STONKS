row = '''
Cost of revenue (COR)

'''
r = str(row).lower()
replace_chars = [',', '(', ')', '.', '-', '–', ' ', "'", '’']

for c in replace_chars:
    r = r.replace(c, '')

print(r)