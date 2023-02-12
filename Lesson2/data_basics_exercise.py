import json

# JSON string is our data
data_string = '{"name": "Antonio", "current_age": 44, "current_year": 2023, "birth_year": 1978, "age_first_computer": 8}'

# deserializes into dict 
# and returns dict.
data = json.loads(data_string)


# Using the data given write a function that calculates the year when Antonio got his first computer.
# While there is no other person data do check that name is in fact "Antonio" and else return a string of "No user data found".