# Chapter Seven:  String Fundamentals
## Intro to Strings
Strings in Python are immutable sequences, meaning that they have an ordered position (each letter character has a position in the string) and they cannot be changed once created.  Strings can be expressed with
 + 'single quotes'
 + "double quotes"
 + '''...triple quotes...'''
 + 'escape\nsequences'
 + r"raw\strings\"
 + Byte/Unicode literals

Along with sequential operations, strings have the following availble operations and 43 methods:

| Operation | Interpretation |
|------|----|
| '' | empty string |
| "test" | same as 'test' |
| 's\np\ta\x00m' | backslashes are escape sequences |
| """...multiline...""" | triple quoted string blocks |
| r'\temp\folder' | raw strings w/ no escapes |
| b'test' | byte string |
| u'sp\u00c4m' | unicode string |
| 'the %s test' % x | x will be the string printed at %s |
| 'the {0} test'.format(kind) | format string |
| s.find('th') | will find first occurance of a string |
| s.rstrip() | removes whitespace |
| s.split(',') | splits string on the delimiter |
| s.isdigit() | tests if its a digit |
| s.lower() | makes the string all lowercase |
| s.endswith('test') | checks if string ends with 'test' |
| s.endswith('test') | checks if string ends with 'test' |


### Using single and double quotes
Single and double quotes can both be used in python.  This makes it easier to include strings that have either symbol in them without using an escape backslash.
```python
s = "That's an example"         # the ' won't mess up the "" set defining the string
s = '"This quote"'              # '' defines the string so "" will print
s = '"That\'s a quote"'         # \ escape is needed since there are both " and '

```
### Escape sequences
The backslash \ is used to denote special characters in strings.  In the last example, we had to use one to tell Python that we wished to use **'** as a character and not as the 'begin-end string' command.  

| Escape |  |
|-----|-----|
| \newline | just continutes a line |
| \\ | stores a single \ character |
| \' | stores a single ' character |
| \" | stores a single " character |
| \a | makes an alert tone if sound is configured |
| \b | backspace |
| \f | formfeed |
| \n | newline |
| \r | carriage return |
| \t | tab |
| \v | verticle tab |

Escape sequences can allow for binary/octal/hex values to be printed into a string.  
```python
a = '\0a\0b\0c'
print(a,len(a))
#   returns 'abc 6'

b = '\ta\tb\tc'
print(b,len(b))

c = '\x001\x002\x003'
print(c,len(c))
```
### Raw strings
These are used to minimize the amount of backslashes that arise in certain strings (especailly in regular expressions.)  They have the format:
```python
a = r'raw string here: \t\n is printed'
```
If we wanted to open a file, raw strings can help simplify the string 
```python 
file = open(r'C:\home\path\','w')
file = open('C:\\home\\path\\','w')
```
### Multiline strings using """
Use triple quotes to write out a multi-line string.  These can be used for multi-line messages and also for writing long comments in code.
```python
a = """multi
line
string
"""
print(a)

```
## Using Strings
### Basic operations
In chapter 4, we saw some very easy string manipulations
```python
a = 'abc'
print(len(a))
print(a+'def')
print(a*3)
```

There are also many ways of testing the contents of a string to get a True or False value for a control sequence.
```python
a = 'test string'
print('str' in a)       returns True
print()
```


### Indexing and slicing
In Python, characters are just a string containing a single letter.  Strings with multiple characters can be addressed by using their place within a string similar to a list.  They can also be addressed with negative indicies, indicating going from right to left.
```python
a = 'test string'
print(a[1], a[-1])
print(a[1:-1])
```

Python also allows for a third index, which is the step.  Notice how the string below skips over every other character in the string:
```python
a = '1234567890'
print(a[0:8])
print(a[::2])
print(a[0:6:2])
```

This can be used to reverse an item:
```python
a = '1234567890'
print(a[::-1])

```
Both of thse cases can be expressed as slices:
```python
a = 'test string'
print(a[(slice(2,6))])
print(a[slice(None, None, -1)])

```
### String conversion
Convert a string to an int
```python
a = '25'
b = 5 + int(a)      
print(b)
```
Convert an int to a string
```python
a = 3
b = 8
c = repr(a+b)
d = repr(a)+repr(b)
print(c,d)
```
If you need to convert floats instead of ints, just use `float()` instead of `int()` in the examples above.

`ord` will convert a character to it's ascii code, and `chr` will go from ascii code to character string.
```python
a = ord('t')
print(a)
print(chr(a))
```
In the next example, a string of ones and zeros representing binary data will be converted to binary, then the binary number will be used by ord to print out a string. 
```python
b = '11011'
i = 0
while b !='':
    i = i*2 + (ord(b[0]) - ord('0'))
    b = b[1:]    
print(i) 

```


### Changing strings

To change a string, we have to construct a new string with our changes in place.  All of the previously mentioned string operations can be used to do this!  Many other ways are presented here.

```python

```

## Strings Methods

## Formatting


## General Type Categories
