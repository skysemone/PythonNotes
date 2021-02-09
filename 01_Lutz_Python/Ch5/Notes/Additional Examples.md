# Chapter Four:  Additional Examples


### Example 1:  Using matplot lib to print out a scatter chart.  Note that the size of the points used scales to the number of points plotted.  This code will try to determine the value of pi by counting the ratio of random points inside the first quadrant of a circle.
---
```python 
'''
Created on Jan 31, 2021

@author: Sky Semone

Example one:  using matplotlib.  This code slow at plotting >10,000 points
'''


#Plotting the random points:
import matplotlib.pyplot as plt
import random
inside = 0
i=1
n=int(input('Enter the total number of points: '))
msize=markersize=40/(n**0.5)
while (i<=n):
    x = random.random()
    y = random.random()
    if ((x**2)+(y**2))<=1:
        inside+=1
        plt.plot(x , y , 'go', markersize=msize)
    else:
        plt.plot(x , y , 'ro', markersize=msize)
    i+=1
    
pi=(4*inside)/n
print ("The value of pi is:")
print(pi)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

```
