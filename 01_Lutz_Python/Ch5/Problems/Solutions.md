# Chaper 5 Problems and Solutions
### 1.)  Evaluate `2 * (3 + 4)`
Parathentical values are determined first, so 2*7=14.
### 2.)  Evaluate `2 * 3 + 4`
Multiplication is performed first, so 6+4=10.
### 3.)  Evaluate `2 + 3 * 4`
Again, multiplication is first, so its 12.
### 4.)  What tools can be used to find the square root, what tools can be used to find the square of a number?
`math.sqrt(x)` can give the square root, and using x**2 will give x squared.  Using `pow(x,n)` will give the square root if n=0.5 or the square if n=2.
### 5.)  What type is the evaluation of `1 + 2.0 +3`
Floating point
### 6.)  How can you truncate and round a floating number?
|truncate|int(n), math.trunc(n)|
|round|round(n, digits)|
|floor|math.floor(n)|
### 7.)  Convert an int to a float.
float(int), or use it with floats in an expression
### 8.)  How would you display an integer in octal, hex, and binary notation.
oct(int), hex(int)
### 9.)  Convert octal, hex, binary string to a base 10 string.
int(s, base) function does the job.  The eval(s) function can be used as well but has security issues and takes up more resources
