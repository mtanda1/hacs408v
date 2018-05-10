import os
import re
import csv
import pandas as pd

CORE_DFRAME = None

def load_data(path='./lists/merged-withcounts.csv'):
    global CORE_DFRAME

    CORE_DFRAME = pd.read_csv(path, sep='\t')

def marcos_shit():
    global CORE_DFRAME
    df_complex = pd.dataframe(columnns = ['passwd','complexity']) 
    #writer = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
    for line in CORE_DFRAME[passwd]:
        #line=line.strip()
        comp = 0
        for char in line:
            if re.match(r'[a-zA-Z]', char):
                comp = comp +26
            if re.match(r'\d',char):
                comp = comp + 10
            if re.match(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]',char):
                comp = comp + 33
        #row = line[0] +','+ line[1]+',' + str(comp)
        df_complex.append(passwd,comp)
    # Do shit
    return(df_complex)

def main():
    load_data()
    output_dframe = marcos_shit()
    print(output_dframe)

main()






import os
import re
import csv
import pandas as pd
def fuuuuuuuckkkkkkk(csvfile):
with open(csvfile,'r') as infile, open("complexity.csv", 'w') as outfile:
    #with open("HACS408V-netflow-host1-ssh.txt",'r') as infile, open("cleannetflowh1.csv", 'w') as outfile:   merged-withcounts
    df_complex = 
    writer = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
    for line in infile.readlines():
        #line=line.strip()
        line = line.strip().split('\t')
        comp = 0
        for char in line[1]:
            if re.match(r'[a-zA-Z]', char):
                comp = comp +26
            if re.match(r'\d',char):
                comp = comp + 10
            if re.match(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]',char):
                comp = comp + 33
        row = line[0] +','+ line[1]+',' + str(comp)

        writer.writerow(row.split(','))
        #print(comp, line[1])

def load_data(path='./lists/merged-withcounts.csv'):
global CORE_DFRAME
CORE_DFRAME = pd.read_csv(path, sep='\t')
fuuuuuuuckkkkkkk("merged-withcounts.csv")      
