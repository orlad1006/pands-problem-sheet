#week3_task
#Author: Orla Dowling
#python_accounts.py
# Write program that reads in a 10 character account number and outputs account number with only the last
# 4 digits showing e.g. xxxxxx2589

from dataclasses import replace


accountnum = str(input("Please enter a 10 digit account number:  "))

print("XXXXXX" + accountnum[6:])


#modidy the program to  deal with account numbers of any lenght
# print last 4 digits only
# all characters to position -5 replace with X

initial_digits= (accountnum)[0:-5]
last_4_digits = (accountnum)[-4:]   

print(last_4_digits)




  













