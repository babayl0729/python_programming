# Tuple-an ordered collection or grouping of items.
# Tuples are faster than lists.
# it is immutable cannot be changed.
# valid keys in a dictionary
# some methods return them to you - 
# like .items() when working with dictionaries.

# x = (1,2,3,4)
# # TypeError: 'tuple' object does not support item assignment
# x[0] = 9
# print(x)

# alphabet = ('a','b','c','d','e')
# # no append in tuple
# print(alphabet.append('f'))

# Creating/Accessing
y = (1,2,3,3,3)
print(y[2])#3
print(y[1])#2
print(y[-1])#3

#Tuples can be used as keys in dictionaries:
locations = {
    (35.6895,39.6917): "Tokyo Office",
    (40.7128,74.0060): "New York Office",
    (37.7749,122.4194): "San Francisco Office"
}
print(locations[(37.7749,122.4194)])

# you cannot use a list in a Tuples
# loc ={
#     [35,39]: "Tokyo Office"
# }
# #TypeError: unhashable type: 'list'
# print(loc)

# some dictionary methods like .items() return tuples
cat = {"name":"biscuit","age":0.5,"favorite_toy":"toys"}
print(cat.items())



