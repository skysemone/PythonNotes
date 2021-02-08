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
#### Number-theoretic and representation functions
+ `math.ceil(x)`                ceil function, next integer greater than x
+ `math.comb(p,q)`            choose p items from q, n! / (k! * (n - k)!) when k <= n
+ `math.factorial(x)`      x!
+ `math.gcd(x)`                  greatest common denominator, x is an int
+ `math.isclose(a,b)`      true if a,b are close.  optional arguments rel_tol, abs_tol
+ `math.trunc(x)`              truncate x to integer
#### Constants
+ `math.pi` = 3.14....
+ `math.e` = 2.718....
+ `math.tau` = 6.283....
+ `math.inf` == float('inf')
+ `math.nan`  == float('nan')

#### Special functions
+ `math.erf(x)`               error function
+ `math.erfc(x)`             complimentry error function
+ `math.gamma(x)`           error function
+ `math.lgamma(x)`         natural log of the absolute value of the gamma function
+ `math.dist(p,q)`         returns the euclidean distance between points i.e. sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

#### Power and logarithmic
+ `math.sqrt(x)`             square root
+ `math.exp(x)`               exponential function
+ `math.expm1(x)`           exp(x)-1, but more accurate
+ `math.log(x, [b])`     log of x, using optional base b


#### Trig and hyperbolic functions
+ `math.sin(x)`, `math.cos(x)`,`math.tan(x)`,  `math.asin(x)`, `math.acos(x)`, `math.atan(x)`
+ `math.sinh(x)`, `math.cosh(x)`,`math.tanh(x)`,  `math.asinh(x)`, `math.acosh(x)`, `math.atanh(x)`
+ `math.radians(x)` = degrees to radians
+ `math.degrees(x)` = radians to degrees

### 'random'
There are many advanced things you can do with this module, but for most instances, just a regular pseudo-random number will work just fine.  It's been noted that this module should not be used for making keys, or for anything meant to be secure, but will work just fine for math and statistics simulations (see the extra examples and problems for this chapter.)

To make a random integer over a range, use 
```python
import random
for x in range(0, 10):
    print(random.randint(0,10))
```
Other useful functions include
+ `random.random()`               random float between 0 and 1
+ `random.uniform(a,b)`       random float between a,b
+ `random.gauss(mu,sig)`     random number based on the Gaussian distribution

### 'cmath'
Complex numbers are included with Python, but this module contains many of the tools needed to work with them outside of basic addition and multiplication, etc.  Many of the trig functions available in the `math` module have complex variants here.
+ `cmath.phase(x)`                 argument of x, `math.atan2(x.imag, x.real)`
+ `cmath.rect(x)`                   goes from polar to rectilinear coordinates.
+ `cmath.polar(x)`                 gives the complex value in r, phi


