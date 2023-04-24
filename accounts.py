#week3_task
#Author: Orla Dowling
#python_accounts.py
# Write program that reads in a 10 character account number and outputs account number with only the last
# 4 digits showing e.g. xxxxxx2589
#modidy the program to  deal with account numbers of any lenght
#from dataclasses import replace - cound not get tis to work

#Attempt 1: 
#accountnum = str(input("Please enter a 10 digit account number:  "))

#print("XXXXXX" + accountnum[-4:])

#Feedback from Andrew : modidy the program to  deal with account numbers of any lenght

#Attempt 2: 

account_num = str(input("Please enter a 10 digit account number:  "))
# we need to determine how many digits in the account number as it is not defined      
num_of_digits = len(account_num)
#print (num_of_digits) to check

num_of_X = num_of_digits -4 # so we now can work out how many X's I need by subsracting 4 (last 4 digits)
#print(num_of_X) to check

cover_letter = ('X') # made X a variable - string - easier to multiple by the lenght - last 4 digits

start = (cover_letter*num_of_X) # this is the start of the account number  that we want to return
#print (start) to check 
last_4_digits = (account_num[-4:]) # this is splicing the account numbers from the 4th last digit to the end
#print(last_4_digits) 

print (f"Your account number is {start}{last_4_digits}") # Print out the account number string with
#no gaps between start and last 4 digits

       












  













