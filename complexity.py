import os
import re
import csv
import pandas as pd

CORE_DFRAME = None

def load_data(path='../lists/test.csv'):#merged-withcounts.csv
    global CORE_DFRAME

    CORE_DFRAME = pd.read_csv(path, sep='\t')

def complexity():
    global CORE_DFRAME
    #print(CORE_DFRAME)
    df_complex = pd.DataFrame(columns = ['count','passwd','complexity']) 
    rows = []
    #writer = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
    for row in CORE_DFRAME.itertuples():
        
        passwd = str(getattr(row, 'passwd'))
        count = getattr(row, 'count')
        #print(passwd)
        comp = 0
        for char in passwd:
            if re.match(r'[a-zA-Z]', char):
                comp = comp +26
            if re.match(r'\d',char):
                comp = comp + 10
            if re.match(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]',char):
                comp = comp + 33
        
        rows.append({'count':count,'passwd':passwd, 'complexity':comp})
    #print(rows)
    df_complex = df_complex.append(rows)
    #print(df_complex)
    return(df_complex)

def main():
    load_data()
    output_dframe = complexity()
    print(output_dframe)

main()




