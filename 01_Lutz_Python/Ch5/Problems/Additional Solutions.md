# Solutions to Additional Problems
This is just the contents of the Additional Solutions folder all on one page

### 1.) Using the code from example one and a for loop, make a program that prints out the estimation of pi for n = 10, 100, ... ,a million number of points.  Do not try to make a plot for this (remove everything related to the plot.)
---
``` python
'''
Created on Jan 31, 2021

@author: Sky Semone

Solution one:  this will plot 10^1 to 10^6 points and print the values
'''
import random

inside = 0
i=1
for p in range(1, 7):
    n=10**p
    while (i<=n):
        x = random.random()
        y = random.random()
        if ((x**2)+(y**2))<=1:
            inside+=1
        i+=1
    pi=(4*inside)/n
    print ('Using 10^',p,' points, pi is:  ', pi)

```
