import csv
import argparse

def parsecsv(myfile):
    mydict = {}
    
    # parse the CSV file into a dictionary and retrun it
    with open(myfile, mode='r') as infile:
        # Each row read from the csv file is returned as a list of strings
        reader = csv.reader(infile)
        for rows in reader:
            # Convert strings to upper case, in case the two files has different case
            # This is the key, the first column in each row
            k = rows[0].upper()
            # if this row contains more than one column
            if len(rows) > 1:
                v = rows[1].upper()
            else:
                # if this row contains only one column (There will be no value for the key, then create a dummy value
                rows.append('Null value')
                v = rows[1].upper()
            
            # Create dictionary, for each row: key is first column, value is second column
            mydict[k] = v
        
        return mydict

parser = argparse.ArgumentParser('userdig')
parser.add_argument('-r', '--reference', required = True, type = str , metavar = '', help = 'Reference CSV file containing all data' )
parser.add_argument('-f', '--findlist', required = True, type = str ,  metavar = '', help = 'CSV file containing users to find' )
parser.add_argument('-o', '--output', required = False,default = 'output.csv', type = str , metavar = '', help = 'Full path to output file' )
args = parser.parse_args()

def main():
    
    #launch my created function parsecsv (on reference file), it returns a dictionary (reference dictionary)
    ref = parsecsv(args.reference)
    #launch my created function parsecsv (on users file), it returns a dictionary (users dictionary)
    lookup = parsecsv(args.findlist)
    with open(args.output,'w') as outfile:
        # Compare key in dictionaries to find which key exists in the two dictionaries
        for x in lookup.keys():
            if x in ref.keys():
                # Manually construct the CSV lines
                linez = '\"' + x + '\"' + ',' + ref[x]
                outfile.write(linez + '\n')
               
                                
            else:
                linez = '\"' + x + '\"' + ',' +'Not found'
                outfile.write(linez + '\n')
    print('done')            

if __name__ == "__main__" : main()
