# Chapter Five:  Numeric Types

## Basics



This book presents numeric data types before strings, lists etc since numbers are so fundamental to structuring and expressing objects in Python.  While the book goes into great detail explaining the underlying mathematics, I will assume a basic understanding of discrete mathematics to direct this section of notes toward application.

Many of the mathematical hammers used in Python need to be imported from numpy and other modules; these are consequentially excluded from most of the book and these set of notes.    The built in functions and modules for mathematical objects in Python include:
 + round
 + math
 + random
 
 When printing, Python allows for 'printf' type display options. 
 ```python
 a=1.0/3.0
 print(a)   #lots of digits
 print('%e' % a)        #exponential with many digits
 print('%4.2f' % a)     #floating point w 2 decimals
 ```
 
## Types of Numbers

+ Integers
+ Hex, Octal, Binary literals
+ Complex 
+ Fractions
+ Decimals

## Evaluation Differences Between Python2 and Python3
Dividing integers in python3 now returns a float.
| Expression | Python 2 | Python 3|
| ------ | ----------- | ---------- |
| `10/4`  | 2 | 2.5 |
| `10/4.0` | 2.5| 2.5 |
| `10//4`    | 2 | 2 |
|`10//4.0`  | 2.0 | 2.0 |

## Simple Discrete Math Examples 

 
## Complex Numbers
The imaginary part of the complex number can be expressed by **j** or **J**.  A few examples of mathematics with complex numbers follows.  There is also a standard module **cmath** which will be discussed at the end of this section.
```python
print((1+1j)*(1-1J)) 
print(1.1*54.2*(1j-7))
```

## Hex, Octal, Binary
### Expressing and displaying numbers
```python
print(0x01, 0x20, 0xFE, 0xfe)   #hex literals
print(0o1, 0o20, 0o333)         #octal literals 
print(0b01, 0b11, 0b11111111)   #binary literals

print(hex(32))                  #convert base 10 to base ___
print(oct(32))
print(bin(32))
```
The `eval` function in Python is useful here; it takes a string as argument and runs the string as Python code.
```python
print(eval('32'))           #prints out '64'
print(eval('0x20'))
print(eval('0o40'))
print(eval('0b100000'))
```
Numbers of different bases can be shown or converted using the following print statements:
```python
print('%o, %X, %x '%(31,31,31))             #this way does not support binary
print('{0:o},{1:x},{2:b}'.format(31,31,31)) #this way supports binary
```

### Operations
These are useful for dealing with binary data

These are some simple examples of bitwise operations:
```python
x=1                 # this is 0001
print(x<<2)         # shift left 2 bits; 0100=4
print(x|2)          # bit or, 0011=3
print(x&7)          # bit and, 0001=1
print(x^0111)       # bit xor, 0110=6
```
## Decimals and Fractions
### Decimals
Decimals are fixed-precision floating-point values.  At the risk of taking more computational inertia, these allow for more accurate arithmatic without the standard machine error.  For Python 3.3 and later, the Decimal type has been optimized to be 10-100 times faster.

```python
from decimal import Decimal
print(0.1+0.1+0.1-0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
```

The **decimal** module can also be used to set the decimal precision manually
```python
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
```
### Fractions
This implements rational numbers incase we need to preserve the exact quantity expressed in a fraction
```python
from fractions import Fraction
a = Fraction(1,2)
b = Fraction(2/3)
print(a*b, a/b,a+b)
```


## Sets
Sets in python can only be made in immutable objects.  Sets are useful for grouping things together and for making comprehensions.
```python
a = {2, 4, 6, 8}
print(a & {1,2,3,4})               #intersection
print(a | {1,2,3,4})               #union
print(a - {1,2,3,4})               #difference
print(a > {2,6})                   #superset
```
In this example a set is used to filter out the duplicate items in a list.
```python
l1 = [1,2,3,4,5,6,7,1,2,3]
set(l1)
l2 = list(set(l1))
print(l2)
```

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

### 'math'


#### Constants
+ `math.pi` = 3.14....
+ `math.e` = 2.718....
+ `math.tau` = 6.283....
+ `math.inf` == float('inf')
+ `math.nan`  == float('nan')

#### Special Functions

### 'random'

### 'cmath'
