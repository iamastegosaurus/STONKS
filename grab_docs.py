import os
import shutil

def grab_auto(path):

    stocks = os.listdir(path)

    # TODO replace hardcoded auto
    doc_name = 'auto' 

    for s in stocks:
        p = path + s + '/' + doc_name + '.xlsx'
        newpath = 'Q:/STONKS/auto/' + s + '.xlsx'
        if os.path.exists(p):
            # if not os.path.exists(newpath):
            shutil.copyfile(p, newpath)
        
    
grab_auto('Q:/STONKS/downloads/')