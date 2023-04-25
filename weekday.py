#Weekday.py
#Author: Orla Dowling
# Write a program that outputs whether or not today is a weekday

import datetime # module to help work with dates as objects 

day= datetime.datetime.today().weekday() # the weekday function of class date returns the day
#of the week as an integer. It starts from 0 for a Monday and ends at 6 for a Sunday
# therefore I can createa program that will decide what statement to print once run using if/else
#and the int value of today

if day<5 :
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")  

