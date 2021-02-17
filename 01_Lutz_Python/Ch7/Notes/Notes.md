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

To change a string, we have to construct a new string with our changes in place.  All of the previously mentioned string operations can be used to do this!  Several other ways are presented here, but I will not cover all of them
```python
a = 'test string'
b = a.replace('t','b')
print(b)
```
String formatting techniques can be implemented to create new strings.  This is especially helpful in strings that have delineated data or words need to be manipulated within a larger string.

```python
a = 'this is a %s with %d words' % ('string', 7)
print(a)

```

## Strings Methods
Methods are made up of *call* and *fetch* functions.  Attribute fetches look like object.attribute, indicates that the attribute is held by the object.  Call expressions look like function(args), meaning that the code labeled as the function will be run with the arguments as parameters.  If we combine both of these things, we get methods.
|Method| |
|-|-|
|capitalize()  |  Converts the first character to upper case|
|casefold()   | Converts string into lower case|
|center()   | Returns a centered string|
|count()  |  Returns the number of times a specified value occurs in a string|
|encode() |   Returns an encoded version of the string|
|endswith() |   Returns true if the string ends with the specified value|
|expandtabs()  |  Sets the tab size of the string|
|find() |   Searches the string for a specified value and returns the position of where it was found|
|format()  |  Formats specified values in a string|
|format_map()  |  Formats specified values in a string|
|index()  |  Searches the string for a specified value and returns the position of where it was found|
|isalnum()   | Returns True if all characters in the string are alphanumeric|
|isalpha()  |  Returns True if all characters in the string are in the alphabet|
|isdecimal()   | Returns True if all characters in the string are decimals|
|isdigit() |   Returns True if all characters in the string are digits|
|isidentifier()  |  Returns True if the string is an identifier|
|islower()  |  Returns True if all characters in the string are lower case|
|isnumeric()   | Returns True if all characters in the string are numeric|
|isprintable()   | Returns True if all characters in the string are printable|
|isspace()   | Returns True if all characters in the string are whitespaces|
|istitle() |   Returns True if the string follows the rules of a title|
|isupper()  |  Returns True if all characters in the string are upper case|
|join() |   Joins the elements of an iterable to the end of the string|
|ljust() |   Returns a left justified version of the string|
|lower()  |  Converts a string into lower case|
|lstrip()  |  Returns a left trim version of the string|
|maketrans()  |  Returns a translation table to be used in translations|
|partition()    |Returns a tuple where the string is parted into three parts|
|replace()   | Returns a string where a specified value is replaced with a specified value|
|rfind()  |  Searches the string for a specified value and returns the last position of where it was found|
|rindex()  |  Searches the string for a specified value and returns the last position of where it was found|
|rjust() |   Returns a right justified version of the string|
|rpartition()   | Returns a tuple where the string is parted into three parts|
|rsplit()  |  Splits the string at the specified separator, and returns a list|
|rstrip()  |  Returns a right trim version of the string|
|split()   | Splits the string at the specified separator, and returns a list|
|splitlines()  |  Splits the string at line breaks and returns a list|
|startswith()   | Returns true if the string starts with the specified value|
|strip()  |  Returns a trimmed version of the string|
|swapcase() |   Swaps cases, lower case becomes upper case and vice versa|
|title()  |  Converts the first character of each word to upper case|
|translate()  |  Returns a translated string|
|upper()  |  Converts a string into upper case|
|zfill()   | Fills the string with a specified number of 0 values at the beginning|

### Examples using methods

We can split strings on the occurance of a character.  In the example below, the string will be split manually, and then using the more appropriate method.
```python
#   splitting a string manually
line = 'this is a test line of text'
s1 = line[0:4]
s2 = line[5:7]
print(s1,s2)

```
```python
#   using .split()
line = 'this is a test line of text'
s = line.split()
print(s[0],s[1])
```
By default, `split()` is separating by spaces, but it can separate any string argument.  In the next example, `striip()` is used to remove all of the spaces from the string.  Try removing this to see the difference it makes.
```python
#   using .split()
line = ' this    ,is  ,   1,  2   ,3, 4,   5 , csv'
s = line.split(',')
for i in s:
    print(i.strip())
```


```python


```
```python


```
```python


```



## Formatting
The basics of formatting were already covered in this chapter, but a complete list of codes are given here.  These should be familiar to C programmers.  The general form of the targets in a format string is...
`%[(keyname)][flags][width][.precision]typecode`

|Code| |
|-|-|
| s | string or str(x) |
| r | repr or repr(x) |
| c |character  |
| d | decimal |
| i | integer |
| o | octal |
| x | hexidecimal |
| X | uppercase hex |
| e | float with exponent |
| E | uppercase float with exponent |
| f | float |
| F | uppercase float |
| g | e or f |
| G | E or F |
| % | literal % |


## Using Regular Expressions for Strings
This section will use resources outside of the Lutz text.
#### What are regular expressions
#### Special characters
These characters will match:
+ **.**   any given character except the newline (DOTALL flag overrides this exception.
+  **^**  the start of a string (and after newlines if in MULTILINE mode)
+  **$**  the end of a string (and before a newline in MULTILINE mode)
+ **\*** 0 or more repetitions of the proceeding RE
+  **+**  1 or more repetitions of the proceeding RE+
+ **?**  0 or 1 repetitions of the proceeding RE
+ **_?** adding '?' after the qualifier match as few character as possible
+ **{m}** m copies of previous RE
+ **{m,n}** m to n copies of previous RE
+ **[]** a set of characters
+ **a|b** set a or set b
+ **\w** words i.e '[a-zA-Z0-9_]'

#### Match
```python
import re
#   match a date string
regex = r'([a-zA-Z]+) (\d+)'
if re.search(regex, "June 24"):
    match = re.search(regex, "June 20")
    print('Match at index %s, %s' % (match.start(), match.end()))
```
#### Findall
```python
import re
txt = 'This is a nice example, isn't it?'
x = re.findall('is', txt)
print(x))
```
```python
import re
regex = r'[a-zA-Z]+ \d+'
matches = re.findall(regex, 'December 21, August 10, January 2')
for match in matches:
    print('Full match: %s' % (match))

```

#### Search

```python 
import re
regex = re.compile(r'(\w+) World')
result = regex.search('Hello World this is a test')
if result:

    print(result.start(), result.end())

for result in regex.findall('1 World, 2 World, red World, blue World'):
    print(result)

print(regex.sub(r"\1 friends", "Hello World"))
```

