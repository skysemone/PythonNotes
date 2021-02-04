# Chapter Five:  Numeric Types

## Basics



This book presents numeric data types before strings, lists etc since numbers are so fundamental to structuring and expressing objects in Python.  While the book goes into great detail explaining the underlying mathematics, I will assume a basic understanding of discrete mathematics to direct this section of notes toward application.

Many of the mathematical hammers used in Python need to be imported from numpy and other modules; these are consequentially excluded from most of the book and these set of notes.    The built in functions and modules for mathematical objects in Python include:
 + round
 + math
 + random
 
 
## Types of Numbers

+ Integers
+ Hex, Octal, Binary literals
+ Complex 
+ Fractions


## Evaluation Differences Between Python2 and Python3
Dividing integers in python3 now returns a float.
| Expression | Python 2 | Python 3|
| ------ | ----------- | ---------- |
| `10/4`  | 2 | 2.5 |
| `10/4.0` | 2.5| 2.5 |
| `10//4`    | 2 | 2 |
|`10//4.0`  | 2.0 | 2.0 |

## Discrete Math Examples 
 
## Complex Numbers

## Hex, Octal, Binary

## Bitwise Operations

## Decimals and Fractions

## Sets

## Booleans
Python has the data type **bool** that gives us an easy way of expressing True and False.  True corresponds to the value '1' or something existing, while false corresponds to 0; if presented with other integers they will take on this integer value.

```python
#   1 and True are the same, 0 and False are the same
print(1 == True, 0 == False)

#   1 and True are different objects though
print(1 is True)

# Adding Trues results in an integer.  In some places this expression might indicate 'true or true' which returns true.  Not here...
print(True + True)
print (True or True)
```

One quick example of how numbers can be used for control logic is here:
```python
#   print out 10, 9, ..... 2, 1.  Guess what happens if you change the line 'x-=1' to 'x-=1.1'
x = 10
while x:
    print(x)
    x-=1
```
## Other Tools
### Included functions

### 'import math'
#### Constants
+ `math.pi` = 3.14....
+ `math.e` = 2.718....
+ `math.tau` = 6.283....
+ `math.inf` == float('inf')
+ `math.nan`  == float('nan')

#### Special Functions
