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
