#Lab Topic 02-Representing Data 
#2 - Write a program to read in the data(data.csv file created) and output each line as a list.
# Author: David Scally

import csv

FILENAME = "data.csv" 
DATADIR = "./"

#with open (DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #for line in reader:
       # print (line)

 #3 Modify the program to deal with the header line separately 

#with open (DATADIR + FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    #linecount = 0
    #for line in reader:
        #if not linecount: # first row e.g header row
            #print(f'{line}\n')
        #else: # all subsequent rows
            #print (line)
          
        #linecount +=1  

  
 #4   4a - Convert the string that is read into an integer  
     # b - Use the quote parameter to read in the numbers as floats 


with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
            pass # first row e.g header row
            
        else:# all subsequent rows
            total += int(line[1])  #first line that is not header
        linecount += 1    # add on to subsequent lines

    print (f"average is {total/(linecount-1)}")
          
         


       


