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

## Loops

A basic loop is `for'
This will be a for each item loop.





