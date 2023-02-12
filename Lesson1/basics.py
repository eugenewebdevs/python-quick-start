# This is a simple example you can run
# Most examples will have notes like this.

# declare a variable
sentence = true

# declare a function
def my_function(data):
    return data + "!!!"

#evaluate the variable
if sentence:
    # notice the indention here
    # Anything at this indention level is in the if statement

    some_work = my_function("I was run in a function")
    
    # run a function with an argument
    print(some_work)
else:
    # if the above if is false print naw
    print("naw")