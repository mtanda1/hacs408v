import os
import re
import csv
def fuuuuuuuckkkkkkk(csvfile):
with open(csvfile,'r') as infile, open("complexity.csv", 'w') as outfile:
    #with open("HACS408V-netflow-host1-ssh.txt",'r') as infile, open("cleannetflowh1.csv", 'w') as outfile:   merged-withcounts
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

fuuuuuuuckkkkkkk("merged-withcounts.csv")      
