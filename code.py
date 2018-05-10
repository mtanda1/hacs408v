import os
import re
import csv
import pandas as pd

CORE_DFRAME = None

def load_data(path='../lists/merged-withcounts.csv'):#merged-withcounts.csv test.csv
    global CORE_DFRAME

    CORE_DFRAME = pd.read_csv(path, sep='\t')
def checklist():
    global CORE_DFRAME
    df_check = pd.DataFrame(columns=['count','passwd','haslowercase','hasuppercase','hasnum','hasspecial']) 
    rows = []
    for row in CORE_DFRAME.itertuples():
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

def complexity():
    global CORE_DFRAME
    df_complex = pd.DataFrame(columns = ['count','passwd','complexity']) 
    rows = []
    for row in CORE_DFRAME.itertuples():
        
        passwd = str(getattr(row, 'passwd'))
        count = getattr(row, 'count')
        comp = 0
        for char in passwd:
            if re.match(r'[a-zA-Z]', char):
                comp = comp +26
            if re.match(r'\d',char):
                comp = comp + 10
            if re.match(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]',char):
                comp = comp + 33
        rows.append({'count':count,'passwd':passwd, 'complexity':comp})
    df_complex = df_complex.append(rows)
    return(df_complex)

def most_complex(df):
    most_complex = 1
    mc = ''
    for row in df.itertuples():
        complexity = int(getattr(row, 'complexity'))

        if(most_complex<complexity):
            most_complex = complexity
            mc = row
    return(mc)
def least_complex(df):
    least_complex = 900000
    lc = ''
    for row in df.itertuples():
        complexity = int(getattr(row, 'complexity'))
        if(least_complex>complexity):
            least_complex = complexity
            lc = row
    return(lc)
def main():
    load_data()
    #checklist_output_dframe = checklist()
    #print(output_dframe)
    complex_output_dframe = complexity()
    most_complex_password = most_complex(complex_output_dframe)
    #least_complex_password = least_complex(complex_output_dframe)
    #print(least_complex_password)
    print(most_complex_password)
main()




