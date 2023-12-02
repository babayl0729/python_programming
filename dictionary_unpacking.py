# using ** as an argument:
# dictionary unpacking

def display_names(first,second):
    print(f"{first} says hello to {second}")
names = {"first": "Colt", "second": "Rusty"}
#display_names(names) # will get an typeerror
display_names(**names)

def add_multiply_nums(a,b,c):
    print(a+b*c)
data = dict(a=1,b=2,c=3)
# add_multiply_nums(data) # typeerror
add_multiply_nums(**data) # 7

def add_multiply_nums2(a,b,c,**kwargs):
    print(a+b*c)
    print("OTHER STUFF...")
    print(kwargs)
data1 = dict(a=2,b=3,c=4,d=55,name="Tony")
# add_multiply_nums(data) # typeerror
# 14
# OTHER STUFF...
# {'d': 55, 'name': 'Tony', 'cat': 'blue'}
add_multiply_nums2(**data1,cat="blue") 
