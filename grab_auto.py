import os
import shutil

def grab_auto(path):

    stocks = os.listdir(path)

    for s in stocks:
        p = path + s + '/auto.xlsx'
        newpath = 'Q:/STONKS/auto/' + s + '.xlsx'
        if os.path.exists(p):
            # if not os.path.exists(newpath):
            shutil.copyfile(p, newpath)
        
        p = path + s + '/auto.py'
        newpath = 'Q:/STONKS/auto/' + s + '.py'
        if os.path.exists(p):
            # if not os.path.exists(newpath):
            shutil.copyfile(p, newpath)


grab_auto('Q:/STONKS/downloads/')