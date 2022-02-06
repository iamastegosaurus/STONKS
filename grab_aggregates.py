import os
import shutil

def grab_aggregates(path):

    stocks = os.listdir(path)

    for s in stocks:
        p = path + s + '/aggregate.xlsx'
        newpath = 'Q:/STONKS/aggregates/' + s + '.xlsx'
        if os.path.exists(p):
            if not os.path.exists(newpath):
                shutil.copyfile(p, newpath)


grab_aggregates('Q:/STONKS/downloads/')