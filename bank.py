# week2_task
# Author: Orla Dowling
#bank.py

#program to add two amounts of money in cents
#input reads in a string so we need to convert it to an integer
#so we can then do mathematical interpretation
#Attempt 1
'''
x = (input("Enter amount 1 (in cent): ")) 
y = (input("Enter amount 2 (in cent) "))

total = float((x/100) + (y/100)) # the total amount

print (f"The sum of these is €{total}")
'''

#Attempt 2 Feedback from Andrew - no floats

x = int(input("Enter amount 1 (in cent): "))
y = int(input("Enter amount 2 (in cent): "))


total = x + y
total_euro = total// 100  # integer division floored 
total_cent = total % 100  # remainder after integer division

print(f"The sum of these is: €{total_euro}.{total_cent:02d}")






      
      

      










