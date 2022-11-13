# Diablo-Line-Drawer
Diablo's Line Drawer is an alternative Line Drawing Algorithm that avoids Heavy Calculations.

The Most Widely and Commonly used Line Drawing Algo is Bresenham's Line Drawing Algorithm,
For all Mordern Computers this is easy to use and fast,accurate,etc.

But for someone like me who makes virtual computers inside videogames like Minecraft
there's alot of divisons and multiplications in Bersenham's Algo which makes computation slower
and also makes the virtual computers physically massive in size.

This Algorithm aims to solve this issue by avoiding multiplications, using comparisions instead of divisons
and using a division alternative that doesn't involve decimal values or fractions.

Also Avoiding heavy calculations inside loops and replacing them with addition and subtraction.

Explanation:  
1)Slope  
Starting with Slope this algo doesn't calculate slope as dx/dy or dy/dx instead it compares if dx==dy ,dx>dy or dy>dx for 3 possible slope cases.

2)Implementing the Simpler Lines  
Not all lines need alot of logic, 45° and similar lines are simply implemented in dx==dy using 4 cases each incrementing or decrementing x and y accordingly.  
Straight Lines just need 2 cases in dy<dx for incrementing or decrementing x and 2 cases in dy>dx for incrementing or decrementing y

3)Implementing the not so Simple Lines
Any Line thats not Straight or 45° i.e. falls anywhere between them needs some tricky math and here's the steps.   
a)Px(Pixels on x) and Py(Pixels on y)  
Px is simply dx+1 and Py is dy+1 , the reason we need these is cuz we need to know how many pixels we are working with so we can evenly distribute the line.  

b)Z(A Scuffed Division for Px and Py)  
This type of division has no name so I call it a scuffed division the idea is to see how many times b can be subtracted from a before a<0.  
First we need to find out which one is greater between Px and Py, for example Px>Py then Px-Py till Px<0  
If Px=8 and Py=3 it will look like 8-3-3-3<0 notice Py had to be subtracted 3 times this gives us Z=3 this means we need 3 pixel long lines while building the bigger line.  

c)OZ(Occurence Of Z)  
OZ is simply how many times we would need that 3 pixel long line in the bigger line, OZ is Delta of Px and Py.  

d)Skips(Number of Pixels to Skip after Plotting a line of Length Z)  
First u need to find smaller one between Px and Py, example if Px>Py then sub+Py-OZ [Sub is a Temporary Variable]  
Skips is the Delta Between OZ and sub.  

e)Preparing Some Variables(x,y,steps and ss)  
x=x1,y=y1, steps=0 is a variable storing number of times the plotting loop runs and ss=0 is a variable used to store skips later.  
