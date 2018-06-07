import csv
import argparse

def parsecsv(myfile):
    mydict = {}
    
    # parse the CSV file into a dictionary and retrun it
    with open(myfile, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            k = rows[0].upper()
            if len(rows) > 1:
                v = rows[1].upper()
            else:
                # if the CSV file contains only one column (There will be no value for the key, then create a dummy value
                rows.append('Null value')
                v = rows[1].upper()
            
            
            mydict[k] = v
        
        return mydict

parser = argparse.ArgumentParser('userdig')
parser.add_argument('-r', '--reference', required = True, type = str , metavar = '', help = 'Reference CSV file containing all data' )
parser.add_argument('-f', '--findlist', required = True, type = str ,  metavar = '', help = 'CSV file containing users to find' )
parser.add_argument('-o', '--output', required = False,default = 'output.csv', type = str , metavar = '', help = 'Full path to output file' )
args = parser.parse_args()

def main():
    ref = parsecsv(args.reference)
    lookup = parsecsv(args.findlist)
    with open(args.output,'w') as outfile:
        # Compare key in dictionaries to find which key exists in the two dictionaries
        for x in lookup.keys():
            if x in ref.keys():
                
                linez = '\"' + x + '\"' + ',' + ref[x]
                outfile.write(linez + '\n')
               
                                
            else:
                linez = '\"' + x + '\"' + ',' +'Not found'
                outfile.write(linez + '\n')
    print('done')            

if __name__ == "__main__" : main()
