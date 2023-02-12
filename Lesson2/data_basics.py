import json

# JSON string is our data
data_string = '{"name": "Antonio", "current_age": 44, "current_year": 2023, "birth_year": 1978, "age_first_computer": 8}'
  
# deserializes into dict 
# and returns dict.
data = json.loads(data_string)

# loops. Lets print out all the keys and values in our data
for key in data:
    value = data[key]
    print("The key and value are ({}) = ({})".format(key, value))

# Lets use the data to answer some a question

# get the data value we will need by the key in the data
antonio_age = data['current_age']


# How many years until antonio is 100?

# function with some math work in it returning the results
def calculate_age(age):
    years = 100 - age
    return years

# pass in the age from the data to the function.
years_to_go = calculate_age(antonio_age)

# print out the results
print("Years to go until Antonio is 100 years old: ", years_to_go)



