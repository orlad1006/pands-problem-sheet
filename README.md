# Pands-problem-sheet  

Author: Orla Dowling

## Week 1:  

Title: helloworld.py  

Task: Print "Hello World"  

## Week 2:  

Title: bank.py  

Task: Create a program that inputs two values in cents and then adds the two amounts and outputs the total in euro and cents  

## Week 3:
Title: accounts.py  

Task: Create a program that inputs a 10 character account number and outputs the account number with only last 4 digits displaying.  

Replace the first 6 digits with X  

My notes:   
I did this by creating a variable that asked the user to input an account number.   then outputed the last 4 digits by using [-4:] and prefixing with 6 'X'. This prints as XXXXXX and the 4 characters counting from the end of the number inputed.   
This worked when I entered the 10 digit number 0123456789 to print out XXXXXX6789. When I inputed a number of with 4 digits or more it printed out as XXXXXX6789 .  

If the number is less than 4 digits it prints out 6'X's and the entered digits  

I spent a lot of time trying to use the inbuilt function replace to replace all characters up to the 4th last digit with 'X' but no matter what I tried it would not run.  It did not like [:-4] as the 'old value' in the replace function.  
https://realpython.com/replace-string-python/  


##    Week 04:  
Title: collatz.py  

Task:  
Write a program called collatz that askes user to input any positive integer.  
It then outputs a number using a calculation based on the current value (user input)
If the user inputs an even number then divide by 2.   
If the user inputs an odd number then multipy by 3 and add one  

My Notes:  
In the first line of code the number is defined as an int and string is used when asking the user to input a positive integer number.  
The first line of code is the  **while loop** . The while loop will execute a set of statements as long as a condition is true . This states that  the code should execute while the number is not equal to 1 . When the number reaches 1 the code will stop running. This is a indefinate iteration as long as the number is not 1.  
The **if** statement will run as long as the statement is true. Statement here is if the number is even (%2==0). Then the number  will be divided by 2 and will be floored (//2). We use the floor function so the number won't have a decimal point when the code runs.  
If this **if** statement is not true the **else** statement will run and take the number and multiple by 3 and add 1.


## Week 5



## Week 6


## Week 7


## Week 8

## Week 9





## REFERENCES  

https://www.markdownguide.org/cheat-sheet/  

https://docs.github.com/en/get-started/writing-on-github  
getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github  

https://www.w3schools.com/python  


## TECHNOLOGY  

Visual Studio Code Version 1.76 (Feb 2023)  

GitHub  

Python  



