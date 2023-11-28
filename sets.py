# set are like formal mathematical sets.
# set do not have duplicate values
# elements in sets aren't ordered.
# you cannot access items in a set by index.
# set can be useful if you need to keep
# track of a collection of elements, but
# don't care about ordering, keys or values
# and duplicates.

# Creating/Accessing

#sets cannot have duplicates
s = set({1,2,3,4,5,5,5})
print(s) # {1, 2, 3, 4, 5}

#creating a new set
s1 = set({1,4,5})
#creates a set with the same values as above
print(s1)

print(4 in s1) #True
print(8 in s1) # False

# Accessing all values in a set
numbers = {1,2,3,4}
for num in numbers:
    print(num)

# Common use case in set
cities = {"Los Angeles", "Baltimore", "Tokyo", "Manila", 
          "Shanghai", "Baltimore", "Calgary", "Tokyo",
          "Manila", "Paris", "Los Angeles"}
# print(set(cities))
# to know unique cities
print(len(set(cities)))
# to list
print(list(set(cities)))




