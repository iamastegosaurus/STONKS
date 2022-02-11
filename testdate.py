def get_date(bad_date):
    bad_date = str(bad_date)
    datestuff = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }

    for mo in datestuff.keys():
        if mo in bad_date.lower():
            month = datestuff[mo]
    day = bad_date.split(' ')[1][:2]
    year = bad_date.split(' ')[2]
    dt = year + '-' + month + '-' + day

    return dt

