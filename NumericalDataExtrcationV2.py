import re
import csv

print 'Enter Name of file you need to Parse e.g. logcat.txt \n'
inputfilename = raw_input('Enter a file name: ')
print 'Enter unique search string e.g aec_process_pack_output \n'
searchstring = raw_input('Enter a search string: ')

matchstring = '(.*)' + searchstring + '(.*)'

inputfile = open(inputfilename, "r")
outputfile = open("parsedata.csv","wb")
out = csv.writer(outputfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

for line in inputfile:
    if re.match(matchstring,line):
        data = map(float, re.findall(r"[-+]?\d*\.\d+|\d+", line))
        print line,
        print data
        print '\n'
        out.writerow(data)  
        
      
inputfile.close()
outputfile.close()

