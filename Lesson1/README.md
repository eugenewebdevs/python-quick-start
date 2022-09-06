# Lesson 1 Foundation Basics

## About

Python is a very approachable programming language. 
The most important concept to understand first is that indention and white space is used as syntax. What this means is that the indention you use must be consistent.

Most other languages use symbolic syntax. Like javascript and curly braces.

 ``` python
 def example:
    return "I did a thing"
```

```javascript
function example(){
    return "I did a thing"
}
```

in python the white space before the return tells the us this is in the function
I js the return is inside opening and closing curly braces to let us know.

we also use the basics of modern programing

- Variables: values stored to be used later
- Conditionals: statements to be evaluated like "if"
- Functions - blocks of code to do work. usually repeatable work.

## Setting Variables

Variables have several types and rules to declaring them. Some don't need anything areound them like numbers others need characters like dictionaries {}. See examples below.

When we need to store a variable it's as easy as:

``` python
my_variable = 2
```

Now we have stored the variebl my_variable as the value of the number 2.

NOTE: It is important to notice the our variable is set to 2 and not "2".

The first is a number and the other is a string.

## Variable Data

Data comes in many types:

- stings: my_variable = "I am a sting of letters"
- numbers: my_variable = 123
- lists: my_variable = ["list", "of", "words]
- dictionaries: my_variable = {"key": "value"}
- boolean: my_variable = True

## Functions

function are a block of code that does some work to return a value

We declare this will be a function with `def`.

Then we name the function. Notice the intention This decides what work to be done is in the function or not.

Some function might take in data to do work on. This is passed inside of ().

Example function : 
``` python
def some_func():
    return "some work"
```
With just this much we can start programming in python. Everything else is mostly building on these and learning patterns and concepts for efficient use.

See all this in action in basics.py