# Pands-problem-sheet  

Author: Orla Dowling  

This document describes and explains my work to solve weekly problem tasks assigned by Andrew Beatty for the Programming and Scripting module for the Higher Diploma in Computing in Data Analytics course
in Atlantic Technological University.  

## Week 1:  

### Title: helloworld.py  

### Task:  
Print "Hello World"  

### References  
https://www.markdownguide.org/cheat-sheet/  
https://docs.github.com/en/get-started/writing-on-github  
getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github  
https://www.w3schools.com/python

## Week 2:  

### Title: bank.py  

### Task:  
Create a program that inputs two values in cents and then adds the two amounts and outputs the total in euro and cents  


### My Notes:  

I want this program to add two amounts of money that is inputted by the user in cents and print out the total in euro and cents. The input reads in a string so I need to convert it to an integer(specifying variable type) so that I can do mathematical calculation on it in cents as a whole number to later convert it to euros and cents.  
Feedback from Andrew: Try not use floats. See attempt 2.   
Using floats when dealing with currency is not ideal as rounding errors can result in significant discrepancies in financial caluculations.  
Attempt 2: To avoid using floats I used floored divison and modulo operators to get euros and cents in two amounts

### References:  
https://martinfowler.com/eaaCatalog/money.html
https://www.w3schools.com/python/python_casting.asp
https://www.stechies.com/floor-division-python/

## Week 3:  

### Title: accounts.py  

### Task:  
Create a program that inputs a 10 character account number and outputs the account number with only last 4 digits displaying.  

Replace the first 6 digits with X  

### My notes:  

Attempt 1  

I did this by creating a variable that asked the user to input an account number then outputed the last 4 digits by using [-4:] and prefixing with 6 'X'. This prints as XXXXXX and the 4 characters counting from the end of the number inputed.   
This worked when I entered the 10 digit number 0123456789 to print out XXXXXX6789. When I inputed a number of with 4 digits or more it printed out as XXXXXX6789 .  

If the number is less than 4 digits it prints out 6'X's and the entered digits  

I spent a lot of time trying to use the inbuilt function replace to replace all characters up to the 4th last digit with 'X' but no matter what I tried it would not run.  It did not like [:-4] as the 'old value' in the replace function.  
https://realpython.com/replace-string-python/    


Attempt 2: 
Feedback from Andrew : what happens if the account number is less than 10 numbers

I created a program that would ask the user to input a 10 digit account umber. If the user did not enter   10 digits then I wanted the program to be able to handle shorter account numbers e.g.  5 to 9 digits.
I split the account number I wanted returned into 2 parts.  


1. Start of account number that is replaced by Xs - number of digits user dependent  


2.Last 4 digits of account number to be displayed  


To take the first part I used the len function to determine the lenght of the account number inputed by the user. I subtracted 4 from the lenght of the number to determine the numbers of X's required. I created 'X' as a string so that it could be repeated easily using the * operator. 

For the second part of the required output Iused th slice function to only didplay the digits from the 4th last position to the end. 

### References:   
https://www.w3schools.com/python/python_variables.asp
https://www.w3schools.com/python/python_strings.asp
https://www.w3schools.com/python/python_strings_slicing.asp
https://www.w3schools.com/python/python_ref_string.asp  
https://linuxhint.com/how-do-you-repeat-a-string-n-times-in-python/



##    Week 04:  

### Title: collatz.py  

### Task:  

Write a program called collatz that askes user to input any positive integer.  
It then outputs a number using a calculation based on the current value (user input)
If the user inputs an even number then divide by 2.   
If the user inputs an odd number then multipy by 3 and add one  

### My Notes:  

I defined the variable number as an integer that the user has to input after a string outlng the question is displayed. 
I used a  **while loop** to execute a set of statements as long as a condition is true . This states that  the code should execute while the number is not equal to 1 . When the number reaches 1 the code will stop running. This is a indefinate iteration as long as the number is not 1.  
I used an **if** statement that will run as long as the statement is true. Statement here is if the number is even (%2==0). Then the number  will be divided by 2 and will be floored (//2). I used the floor function so the number won't have a decimal point when the code runs.  
If this **if** statement is not true the **else** statement will run and take the number and multiple by 3 and add 1.  

Andrew Feedback:  
Each number is outputted to it's own line. 

This is because  the default for the print function is a new line \n.  I used (object, end"" ) in theprint functions to print output on one line.  

### References  
 
https://www.freecodecamp.org/news/python-print-without-new-line-print-on-the-same-line/
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
https://m-nayoumi.medium.com/generating-a-collatz-sequence-using-a-python-program-56c8fbc318c9
https://www.educative.io/edpresso/how-to-generate-the-collatz-sequence-in-python
https://www.w3schools.com/python/python_while_loops.asp  

## Week 5  

### Title:  Weekday.py  

### Task:  

Write a program that outputs whether or not today is a weekday  

### My Notes:  

To begin I imported a module named datetime to work with dates as date objects.  I used functions from the datetime module to define what the day is e.g.  use the datetime.today() function for today's date.  The python weekday function of class date returns the day number of the week as an integer (automatically defaults to an integer). It starts from 0 for a Monday and ends at 6 for a Sunday
Then I used the  **if** and **else** statements to determine whether today is a weekday or weekend.
The code will check if the day is less than 5 (int value) then its a weekday otherwise it is a weekend.

### References:

https://www.w3schools.com/python/python_datetime.asp
https://www.dataquest.io/blog/python-datetime-tutorial/
https://docs.python.org/3/library/datetime.html
https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python


## Week 6  

### Title:  squareroot.py  

### Task:  
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. Create a function called sqrt. Do not use built in functions in this task - research Newtons method of estimating square roots.

### My Notes:  

I wanted a function that would
1. read in a positive float number - user input
2. return the sqaure root of that number - printed out on the terminal

I used Newtons method to create a program that calulates an approximate sqaure root containing a while loop to run through iterations until the best approximation of sqaure root is found.  

Newton's Method:  
Step 1: Assume approx as half the input number given by the user  
approx = 0.5*num  

Step 2:  Find a better value by  
better = 0.5(approx + num/approx)  

Step 3: While better found is not equal to the assumed approx  
    Step 3.1: Assume the found better value as approx approx = better
    Step 3.2: Recalculate better value using better = 0.5*(approx + num/approx)  
Step 4: Print that better value as the square root.

I realise that my code returns quite a poor approximation of the sqaure root. It would be better to use an inbuilt function for an accurate value.  



### References:  
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  
https://www.youtube.com/watch?v=u-OmVr_fT4s
https://www.youtube.com/watch?v=xdlIFw5EM4w
https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/


## Week 7  

### Title: es.py
 
### Task:  

Write a program that reads in a text file and output the numbers of e's it contains.  
The program should take the file name in from an argument on the command line


### My notes:

To read in a text file, the file must already exist or it will throw an error. I chose Little Women
The file to be read should ideally be saved within the same directory as the program, to make it easier to retrieve the file path when typing the name of the text file on the command line.  Therefore I saved a txt file of moby dick from www.guten.org to the pands directory on my desktop

Part 1:  
I imported the sys module to use a Command Line argument.  This is a way of managing the script or program externally by providing the script name and the input parameters from command line options while executing the script. filename = sys.argv[1] equates the name of the file to be read to the first argument on the command line after the name of the script itself. 
  

Part 2: 
I created a function that when called would count the instances of a the letter 'e' in littlewomen.txt with the following steps.

1. Read the file.
2. Store the content of the file in a variable.
3. Use the count() method with the argument as a letter whose frequency is required.
4. Display the count of the letter.


### References  
https://www.gutenberg.org/files/2701/2701-0.txt  
https://www.w3schools.com/python/python_file_open.asp  
https://stackoverflow.com/questions/63066948/how-to-write-a-function-that-takes-in-the-name-of-a-file-as-the-argument-in-pyth  
https://s3-us-west-2.amazonaws.com/oww-files-public/b/b8/HW6syntaxHelper.pdf  
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples  
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/


## Week 8  

### Title: plottask.py  

### Task:  

Write a program called plottask.py that displays:
1. a histogram of a normal distribution of a 1000 values with a mean of  and standard deviation of 2  
2. a plot of the function  h(x)=x3 in the range [0, 10],  
They should be on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc)  

# My Notes:  

Matplotlib is python’s data visualization library which is widely used for the purpose of data visualization.  
Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python  

Part 1: Histogram  

Firstly to draw a plt.hist of a normal distribution I used the random.normal() method for finding the normal distribution of the data. It has three parameters:  
 1. loc – (average/mean) where the top of the bell is located. 
 2. scale – (standard deviation) how uniform you want the graph to be distributed.
 3. size – Shape of the returning Array

The I used np.random.seed(1) to generate the same random numbers each time it is run - easier to debug

I created the program normaldist that when called will generate 1000 random values around the mean of 5 with an SD of 2  

I used print(normaldist) to see that it works before plotting before using the following code to plot the histogram and style it.  



Part 2: Line plot 
The function h(x) = xcubed
I set the x point variable to be an value created in an array from 0 to 10. The y point was the x value cubed. 
Then I plotted x points versus y points and styled the line plot.

Problems: 

I could run the histogram plot and the line plt sepatately and see them clearly but when I ran plt.hist and plt.plot in the same program only the line plot would be visible.  I assumed this was due to the y scale so I changed it from the default linear scale to the log scale.  That way I can see both plots on the one graph.

### References:  
 
https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/  
https://www.geeksforgeeks.org/how-to-plot-a-normal-distribution-with-matplotlib-in-python/?ref=rp  
https://datatofish.com/plot-histogram-python/
https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
https://stackoverflow.com/questions/24519122/how-to-cube-a-number

  


## TECHNOLOGY  

Visual Studio Code Version 1.76 (Feb 2023)  

GitHub  Version 3.7.4 (Jan 2023)

Python  Version 3.11.0 (Jan 2023)



