#Title: es.py
#Author: Orla Dowling 
#Task: Write a program that reads in a text file and out put the numbers of e's

# To read the file from the command line, I needed to import and use the sys module.

import sys

text_file=sys.argv[1] # define the littlewomen .txt as filename. es.py = 0 littlewomen.txt =1 

# This equates the name of the file to be read to the first argument on the command line
#after the name of the python file itself


with open (text_file) as f:
    print (f.read()) #check that the file will read in correctly

#Read the file.
#Store the content of the file in a variable. 
#Use the count() method with the argument as a letter whose frequency is required.
#Display the count of the letter.

def number_of_es(txt_file, letter):
    
    f = open(txt_file, "r")
 
    text = f.read()
 
    return text.count(letter)
 
print(f"Number of es in txt file is: ", number_of_es('littlewomen.txt', 'e'))