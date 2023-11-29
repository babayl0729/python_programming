# add - adds an element to a set. if
# the element is already in the set,
# the set doesn't change.

s = set([1,2,3])
s.add(4)
print(s)

cities = {"Los Angeles", "Baltimore", "Tokyo", "Manila", 
          "Shanghai", "Baltimore", "Calgary", "Tokyo",
          "Manila", "Paris", "Los Angeles"}
cities.add("Vancouver")
print(cities)

# remove - removes a value from the set -
# returns a KeyError if the value is not found
# if you need to avoid keyErrors use .discard()

set1 = {1,2,3,4,5,6}
set1.remove(3)
# set1.remove(7)
set1.discard(7)
set1.discard(4) # removes 4
print(set1)

# copy - creates a copy of the set
s2 = set([1,2,3])
s3 = s2.copy()
print(s3)

# clear - removes all the contents of the set
s4 = set([1,2,3])
s4.clear()
print(s4)

# set math
math_students = {"Isabella", "Leroy", "William", "Raf", "Lorenzo"}
biology_students = {"Leni", "Zander", "Jaiden", "Riley", "Isabella", "William"}

# set union no duplicates
print(math_students | biology_students)

# set intersection will tell me 
# the set of students both of the courses
print(math_students & biology_students)