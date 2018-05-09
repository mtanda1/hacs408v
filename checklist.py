import os
import re
import csv
def fuckoffconnor(csvfile):
	with open(csvfile,'r') as infile, open("checklist.csv", 'w') as outfile:
		#with open("HACS408V-netflow-host1-ssh.txt",'r') as infile, open("cleannetflowh1.csv", 'w') as outfile:   merged-withcounts
	    writer = csv.writer(outfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
	    col = ('count'+',' +'password'+',' +'lowercase'+','+'uppercase'+','+'number'+','+'special_char')
	    writer.writerow(col.split(','))
	    for line in infile.readlines():
	        line = line.strip().split('\t')
	        haslowercase = False
	        hasuppercase = False
	        hasnum = False
	        hasspecial = False
	        if re.search(r'[a-z]', line[1]):
	            haslowercase = True
	        if re.search(r'[A-Z]', line[1]):
	            hasuppercase = True
	        if re.search(r'[\d]', line[1]):
	            hasnum = True
	        if re.search(r'[\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|\]\}\[\{\'\"\;\:\/\\\?\.\>\,\<\ ]', line[1]):
	            hasspecial = True
	        sub = (line[0]+',' +line[1]+',' +str(haslowercase)+','+str(hasuppercase)+','+str(hasnum)+','+str(hasspecial))
	        writer.writerow(sub.split(','))
fuckoffconnor("merged-withcounts.csv")