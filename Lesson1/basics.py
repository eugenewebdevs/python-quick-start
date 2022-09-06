
# declare a variable
sentence = True

def my_function(data):
    return data + "!!!"

#evaluate the variable
if sentence:
    # notice the indention here
    # Anything at this indention level is in the if statement

    some_work = my_function("I was run in a function")
    
    # run a function with an argument
    print(some_work)