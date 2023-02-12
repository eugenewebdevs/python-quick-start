import json

# JSON string is our data
data_string = '{"name": "Antonio", "current_age": 44, "current_year": 2023, "birth_year": 19778, "age_first_computer": 8}'
  
# deserializes into dict 
# and returns dict.
data = json.loads(data_string)