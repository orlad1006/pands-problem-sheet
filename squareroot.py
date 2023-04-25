#Title: squareroot.py
#Author: Orla Dowling
#Task: Write a program that takes a positive floating-point number as input
# and outputs an approximation of its square root
#Note: Can not use a in built function to determine square root
#Suggestion: Newton Method


def sqrt() :  # defining my own function sqrtto take in a positive number
    #and output the sqaure root. I based the sqrt calculation on newtons method.
 
    num = float(input("Please enter a positive number:  "))
    approx = 0.5*num
    better = 0.5*(approx+ (num/approx))
    print(f"The square root of {num} is approx {better}.")

    while (better != approx): 
        approx = better
        better = 0.5*(approx+ (num/approx))
    return better # the retuen value

sqrt() #callig the function


 

