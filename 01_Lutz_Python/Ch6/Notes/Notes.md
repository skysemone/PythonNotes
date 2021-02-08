# Chapter Five:  The Dynamic Typing Interface

## Intro
Notice in Python that the types we are using in code are not explicitly written out and this makes the code usually terse and polymorphic.  Python uses a *dynamic typing model* where types are determined automatically at run-time and not in response to how things are declared (like in statically typed/compiled languages.)

## Variables, Objects, and References
Python lets you code a=3 without declaring types
+  **Variable creation:**  The variable is the name of the object and is created the first time something is assigned to it.  Python can detect some names before the code is run
+  **Variable types:**  Variables never have any information associated with them, they always reference an object.
+  **Variable use:**  When placed in an expression, variables are replaced with the object they reference, so referencing undefined variables will definitely cause an error.

So, to code `x=5`, Python does the following:
1) creates an object with value 5
2) if x does not exist as a variable, make it
3) link x to 5

After this process, we have a more standard system of pointers and references just like many other languages.  Variables are in a table with links to objects and referenced point them to objects are allocated in memory.

Types are defined by the objects, not by the variable.  So if the following code is run the variable name 'x' is just assigned and re-assigned to the objects down the list.
```python
x = 5
x = 'test'
x = 5.5
```

## Garbage Collection and Objects
Garbage collection is the process of freeing up memory for objects that are no longer used.  In the last example program, once x is redefined to the 'test' string, the object representing the integer 5 is no longer needed.  With this example, there really is no need to clean up the few bytes used to allocate a single integer, but with giant lists and dictionaries, this becomes very useful.

Python's memory reclaimation works primarily through reference counters.  Every object keeps track of the number of things that are referencing it; when this number reaches zero, the object is no longer used and can be thrown out.  Python also reclaims cyclic references by default, which are used when an object points to itself.  Non-defualt python implimentations can handle garbage collection differently

## Shared References
 
 ### In-Place Changes
 
 
 ### Equality

## Dynamic Typing


