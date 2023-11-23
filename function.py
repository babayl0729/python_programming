from random import random
# return - exits the function,
# outputs whatever value is placed after the return keyword
# Pops the function off of the call stack

def print_square():
    return 10**2

def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

result = print_square()
print(result)
print(flip_coin())

# Parameters - variables are passed to a function
# think of them as placeholders that get assigned
# when you call the function.

# Parameters vs Arguments
# a parameter is a variable in method definition.
# When a method is called, the arguments are the data
# you pass into method's parameters.
# Parameter is variable in the declaration of function.
# Argument is the actual value of this variable that
# gets passed to function.

def addition(first, second):
    return first + second
print(addition(1,10))

def full_name(first_name,last_name):
    return(f"Your full name is {first_name} {last_name}")
print(full_name('Isabella','Babay'))

# exercise:
def generate_evens():
    # list_[]
    # for x in range(0,50):
    #     if x % 2 == 0:
    #         list_.append(x)
    # return list_
    even = [x for x in range(1,50) if x % 2 == 0]
    return even
evens = generate_evens()
print(evens)

def yell(yelling):
    return yelling.upper()
print(yell("leave me alone!"))




