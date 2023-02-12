# import a package
import json

# JSON string is our data
data_string = '{"name": "Antonio", "age": 44}'
  
# deserializes into dict 
# and returns dict.
data = json.loads(data_string)

# Lets use the data to answer some questions

# get the data value we will need by the key in the data
antonio_age = data['age']

# How many years until antonio is 100?

# function with some math work in it returning the results
def calculate_age(age):
    years = 100 - age
    return years

# pass in the age from the data to the function.
years_to_go = calculate_age(antonio_age)

# print out the results
print(years_to_go)