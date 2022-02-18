
def get_str_date(today, period):
    # if period >= 10:
    # else:
    #     tenyearsago = ''
    
    # if period >= 5:
    # else:
    #     fiveyearsago = ''

    # if period >= 1:
    # else:
    #     oneyearago = ''

    # tenyearsago = str(today.year - 10) + '-' + str(today.month) + '-' + str(today.day)
    # fiveyearsago = str(today.year - 5) + '-' + str(today.month) + '-' + str(today.day)
    # oneyearago = str(today.year - 1) + '-' + str(today.month) + '-' + str(today.day)


    # if today.month <= 3:
    #     threemonthsago = str(today.year - 1) + '-' + str(13 - today.month) + '-' + str(today.day)
    # else:
    #     threemonthsago = str(today.year) + '-' + str(today.month - 3) + '-' + str(today.day)

    # return tenyearsago, fiveyearsago, oneyearago, threemonthsago
    return str(today.year - period) + '-' + str(today.month) + '-' + str(today.day)
