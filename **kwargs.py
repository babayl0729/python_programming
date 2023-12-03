# **kwargs - a special operator we can pass to functions
# gathers remaining keyword arguments as a dictionary
# this is just a parameter - you can call it whatever you want

def fav_colors1(**kwargs):
    print(kwargs)
# {'isabella': 'green', 'jaiden': 'red', 'zander': 'purple'}
fav_colors1(isabella="green",jaiden="red",zander="purple")

def fav_colors2(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
fav_colors2(isabella="green",jaiden="red",zander="purple")
fav_colors2(isabella="green",jaiden="red",zander="purple",william="black")
fav_colors2(rolly="green poop")

def special_hi(**kwargs):
    if "Stew" in kwargs and kwargs["Stew"] == "special":
        return "You get a special greeting Stew!"
    elif "Stew" in kwargs:
        return f"{kwargs['Stew']} Stew!"
    return "Not sure who this is..."
# Hello Stew!
print(special_hi(Stew='Hello'))
# Not sure who this is...
print(special_hi(Yol="hello"))
# You get a special greeting Stew!
print(special_hi(Stew='special'))

# Exercises
def combine_words(words,**kwargs):
    if "prefix" in kwargs:
        return kwargs['prefix'] + words
    elif "suffix" in kwargs:
        return words + kwargs['suffix']
    elif "suffix" in kwargs:
        return words + kwargs['suffix']
    elif "prefix" in kwargs:
        return words + kwargs['prefix']
    return words
# manchild
print(combine_words("child",prefix="man"))
# childish
print(combine_words("child",suffix="ish"))
# worker
print(combine_words("work",suffix="er"))
# homework
print(combine_words("work",prefix="home"))

# Exercise 2 (Walk through solution) By Colt Steele

# Calculate Walkthrough
# This solution uses dict.get() a lot. dict.get('first')  will return the value of 'first' if it exists, 
# otherwise it returns None.  However, you can specify a second argument which will replace None as the default value. 
# I use that in this solution a bunch of times.
#  I defined a dictionary called operation_lookup that maps a string like "add" to an actual mathematical operation 
# involving the values of 'first' and 'second'
# I create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
# Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
# Basically, turning something like "subtract" into:kwargs.get('first', 0) - kwargs.get('second', 0) 
# Which in turns simplifies to a number
# I store the result in a variable called operation_value 
# I return a string containing either the specified message or the default 'The result is' string.  
# Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
# Note: this solution will divide by zero if a 2nd argument isn't provided for divide.  
# You may want to change the default value to 1.  We learn how to handle ZeroDivisionErrors later on in the course.  
# Thanks, Scott for pointing out the issue!

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final

