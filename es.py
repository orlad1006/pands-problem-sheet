#Title: es.py
#Author: Orla Dowling 
#Task: Write a program that reads in a text file and out put the numbers of e's

# To read the file from the command line, we need to import and use the sys module.

#python es.py

import sys


filename=sys.argv[1] # define the modydick.txt as filename. es.py = 0 mobydick.txt =1 

# This equates the name of the file to be read to the first argument on the command line
# (that is, the argument following the name of the python script itself i.e es.py)


with open (filename) as f:
    print (f.read()) #check that the file will read in correctly



def Number_of_E(filename, letter):
    filename=sys.argv[1] 
    with open(filename) as f:
        text = f.read()
        count = 0
     
    for char in text:
          
        if char == letter:
            count += 1
      
    return count
    
  
print(Number_of_E ('filename', 'e'))       

