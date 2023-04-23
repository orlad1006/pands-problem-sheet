#Title: plottask.py
#Author: Orla Dowling
#Task: Write a program called plottask.py that displays:
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], 
#on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc).

import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1) # so random number generated are the same each time
normaldist = np.random.normal(loc=5, scale = 2, size = 1000)
# this will generate 1000 random values around the mean of 5
#with an SD of 2

#print(normaldist) # to see that it works before plotting

xpoints = np.array(range(0,10)) # range of values on the x axis
ypoints = xpoints**xpoints # cube of x

plt.hist(normaldist, color = 'g') # display histogram, green colour
plt.plot(xpoints, ypoints, label = "xcubed", color = "red", ls = "dashed", lw ="2") 

plt.title("Week 8 Task: Learning to Plot", color = 'black') # adds title in black
plt. legend() #shows legend box
plt.grid() # shows grid line
plt.xlabel ("Value (X)", color ="green")
plt.ylabel ("X Cubed", color ="green")

plt.savefig('histplot.png') # Save to PNG file

plt.show() # displays plots


