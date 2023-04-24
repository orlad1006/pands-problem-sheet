# Pands-problem-sheet  

Author: Orla Dowling

## Week 1:  

Title: helloworld.py  

Task: Print "Hello World"  

## Week 2:  

Title: bank.py  

Task: Create a program that inputs two values in cents and then adds the two amounts and outputs the total in euro and cents  


My Notes:  
I want this program to add two amounts of money that is inputted by the user in cents and print out the total in euro and cents. The input reads in a string so I need to convert it to an integer(specifying variable type) so that I can do mathematical calculation on it in cents as a whole number to later convert it to euros and cents.  

Feedback from Andrew: Try not use floats. See attempt 2.   
Using floats when dealing with currency is not ideal as rounding errors can result in significant discrepancies in financial caluculations.  
Attempt 2: To avoid using floats I used floored divison and modulo operators to get euros and cents in two amounts






References:  
https://martinfowler.com/eaaCatalog/money.html
https://www.w3schools.com/python/python_casting.asp
https://www.stechies.com/floor-division-python/






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


Feedback  

References:   
https://www.w3schools.com/python/python_variables.asp
https://www.w3schools.com/python/python_strings.asp
https://www.w3schools.com/python/python_strings_slicing.asp
https://www.w3schools.com/python/python_ref_string.asp  





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


References  

https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

https://www.youtube.com/watch?v=lAp_5qTdOhM

https://m-nayoumi.medium.com/generating-a-collatz-sequence-using-a-python-program-56c8fbc318c9

https://www.educative.io/edpresso/how-to-generate-the-collatz-sequence-in-python


https://www.w3schools.com/python/python_while_loops.asp  

## Week 5  
Title: Weekday.py  

Task: Write a program that outputs whether or not today is a weekday  

My Notes:  

To begin we import a module named datetime to work with dates as date objects.

We then use functions from the datetime module to define what the day is.

For today's date, we use the datetime.today() function from datetime module

The python weekday function of class date returns the day number of the week as an integer (automatically defaults to an integer) . It starts from 0 for a Monday and ends at 6 for a Sunday

Then using the conditional statement if and else we can write the decision making process so that the code will be able to decide whether today is a weekday or weekend.

Then the code will check if the day is less than 5 (interger value that the weekeday function will use) then its a weekday otherwise it is a weekend.

References:

https://www.w3schools.com/python/python_datetime.asp

https://www.dataquest.io/blog/python-datetime-tutorial/

https://docs.python.org/3/library/datetime.html

https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python




## Week 6  
Title:  squareroot.py  

Task:  
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. Create a function called sqrt. Do not use built in functions in this task - research Newtons method of estimating square roots.

My Notes:  

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
    Step 3.2: Recalculate better value using better = 0.5*(approx +         num/approx)  
Step 4: Print that better value as the square root.




References:  
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  
https://www.youtube.com/watch?v=u-OmVr_fT4s
https://www.youtube.com/watch?v=xdlIFw5EM4w
https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/




## Week 7  

Title: es.py
Author: Orla Dowling 
Task: Write a program that reads in a text file and output the numbers of e's it contains.  
The program should take the file name in from an argument on the command line


My notes:  
1. To read in a text file, the file must already exist or it will throw an error 
2. The file to be read should ideally be saved within the same directory as the program, to make it easier to retrieve the file path when typing the name of the text file on the command line.  
3. I saved a txt file of moby dick from www.guten.org to the pands directory on my desktop
4. Command Line argument is a way of managing the script or program externally by providing the script name and the input parameters from command line options while executing the script.

References  
https://www.gutenberg.org/files/2701/2701-0.txt  
https://www.w3schools.com/python/python_file_open.asp  
https://stackoverflow.com/questions/63066948/how-to-write-a-function-that-takes-in-the-name-of-a-file-as-the-argument-in-pyth  
https://s3-us-west-2.amazonaws.com/oww-files-public/b/b8/HW6syntaxHelper.pdf  
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples  
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/


## Week 8  
Title: plottask.py  

Author: Orla Dowling  

Task: Write a program called plottask.py that displays:
1. a histogram of a normal distribution of a 1000 values with a mean of  and standard deviation of 2  
2. a plot of the function  h(x)=x3 in the range [0, 10],  
They should be on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc)  

My Notes:  
Matplotlib is python’s data visualization library which is widely used for the purpose of data visualization.  
Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python  

Part 1: Histogram  

Firstly to draw a plt.hist of normal distribution i will use:  

1. random.normal() method for finding the normal distribution of the data. It has three parameters:  
2. np.random.seed(1) to generate the same random numbers each time it is run - easier to debug
3. loc – (average/mean) where the top of the bell is located.
4. Scale – (standard deviation) how uniform you want the graph to be distributed.
5. size – Shape of the returning Array

 so i created the following program   
    normaldist = np.random.normal(loc=5, scale = 2, size = 1000)  
This will generate 1000 random values around the mean of 5 with an SD of 2  

I used print(normaldist) to see that it works before plotting before using the following code to plot the histogram and style it.  



Part 2:






References:  
https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/  
https://www.geeksforgeeks.org/how-to-plot-a-normal-distribution-with-matplotlib-in-python/?ref=rp  
https://datatofish.com/plot-histogram-python/
https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
https://stackoverflow.com/questions/24519122/how-to-cube-a-number

## REFERENCES  

https://www.markdownguide.org/cheat-sheet/  

https://docs.github.com/en/get-started/writing-on-github  
getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github  
https://www.w3schools.com/python  


## TECHNOLOGY  

Visual Studio Code Version 1.76 (Feb 2023)  

GitHub  

Python  



