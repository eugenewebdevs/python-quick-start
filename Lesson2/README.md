# Lesson 2 Working With Data Basics

## About

Now that we can declare variables or functions, and conditionally make choices lets start manipulating data.

## Packages

Python has many packages built in to handle common operations.

For example the key value data format of JSON.

example: '{"name": "Antonio", "age": 44}'

to read these key and value pairs we can import a package that is ready to help us extract data. We can simply bring in 

`import json`

and then start using the python built in functions.

Example:
``` python
# JSON string is our data
data_string = '{"name": "Antonio", "age": 44}'
# deserializes into dict 
# and returns dict.
data = json.loads(data_string)`
```

There are many built in functions and a whole world of packages to help with data, math, etc...

## Logical Operators

- `and` 	Returns True if both statements are true. Example: `x < 5 and  x < 10	`
- `or`	Returns True if one of the statements is true. Example: `x < 5 or x < 4	`
- `not`: Reverse the result, returns False if the result is true. Example: `not(x < 5 and x < 10)`




