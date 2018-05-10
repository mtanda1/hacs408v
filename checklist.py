import os
import re
import csv
import pandas as pd

CORE_DFRAME = None

def load_data(path='../lists/test.csv'):#merged-withcounts.csv
    global CORE_DFRAME

    CORE_DFRAME = pd.read_csv(path, sep='\t')

def checklist():
    global CORE_DFRAME
    #print(CORE_DFRAME)
    df_check = pd.DataFrame(columns=['count','passwd','haslowercase','hasuppercase','hasnum','hasspecial']) 
    rows = []
    #print(CORE_DFRAME)
    #writer = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
    for row in CORE_DFRAME.itertuples():
        #print(row)
        passwd = str(getattr(row, 'passwd'))
        count = getattr(row, 'count')
        haslowercase = False
        hasuppercase = False
        hasnum = False
        hasspecial = False
        if re.search(r'[a-z]', passwd):
            haslowercase = True
        if re.search(r'[A-Z]', passwd):
            hasuppercase = True
        if re.search(r'[\d]', passwd):
            hasnum = True
        if re.search(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]', passwd):
            hasspecial = True
        rows.append({'count':count,'passwd':passwd, 'haslowercase':haslowercase,'hasuppercase':hasuppercase,'hasnum':hasnum,'hasspecial':hasspecial})
    df_check = df_check.append(rows)
    return(df_check)
def main():
    load_data()
    output_dframe = checklist()
    print(output_dframe)

main()


