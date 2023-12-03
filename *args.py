# *args - a special operator we can pass to functions
# gathers remaining arguments as a tuple
# This is just a parameter - you can call it whatever
# you want!

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all_nums(1,2,3,4))
print(sum_all_nums(5,10,15,20,25,30))

def ensure_info_correct(*args):
    if "Isabella" in args and "Babay" in args:
        return "Welcome back Isabella!"
    return "Not sure who you are"
print(ensure_info_correct("hello",False,78)) # "Not sure who you are"
print(ensure_info_correct(1,True,"Babay","Isabella"))

# exercise

def contains_purple(*num):
    if "purple" in num:
        return True
    return False
print(contains_purple(25,"purple")) # True
print(contains_purple("green",False,37,"blue","hello world")) # False
print(contains_purple("purple")) # True
print(contains_purple("a",99,"blah blah blah",1,True,False,"purple")) # True
print(contains_purple(1,2,3)) # False