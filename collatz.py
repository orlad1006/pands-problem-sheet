# collatz.py
# Author: Orla Dowling

# write a program that askes user to input any positive integer
# then outputs the calculation based on the current value (user input)
#if even divide by 2
#if odd : multipy by 3 and add one


number = int(input("Please enter a number(any positive integer):  "))
#print (number)
# calculate the next value based on  dividing the current value by 2 if even 

while number !=1:# this loop will ensure code will run until number reaches 1
    
    if number % 2 == 0:  # this division will be used when number is even
        number= number//2
        print(number,end="")# to print all on the same line as per feedback

    else: # everthing that isn't even is odd
        number=  3 * number + 1
        print(number,end="") # to print all on the same line as per feedback




