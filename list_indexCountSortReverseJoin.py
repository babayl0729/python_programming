# index-returns the indez of the specified item in 
# the list.
# Can also specify start and end

names = ["Isabella", "Jaiden", "Zander", "William", "Randy", "Woody"]
print(names.index("William")) # 3
print(names.index("Isabella")) # 0

print("-------------index^------------------")

names1 = ["Greg", "Ana", "Ralf", "Greg", "Ant", "Ant", "Ana", "Sophie", "Ralf"]
print(names1.index("Greg")) # 0
# the 1 is the startpoint.
print(names1.index("Greg", 1)) # 3
# The 2 is the startpoint and 8 is endpoint.
print(names1.index("Ana", 2, 8)) # 6

print("-------------count------------------")

# count-return the number of times x appears in the list.
names2 = ["Greg", "Ana", "Ralf", "Greg", "Ant", "Ant", "Ana", "Sophie", "Ralf"]
print(names2.count("Greg"))
print(names2.count("Larry"))
print(names2.count("Ant"))

print("-------------reverse------------------")

# reverse-reverse the elements of the list(in-place)
names3 = ["Loyd", "Andy", "Selena", "Shanaya", "Indu", "Nesty"]
names3.reverse()
print(names3)

print("-------------sort------------------")

# sort-sort the items of the list(in-place)
names4 = ["Loyd", "Andy", "Selena", "Shanaya", "Indu", "Nesty"]
names4.sort()
print(names4)

print("-------------join------------------")

# join-tecnically a String method that takes an iterable argument.
# cocatenates(combines) a copy of the base string brtween
# each item of the iterable.
# returns a new string.
# can be used to make semtences out of a list of words by
# joining on a space.

sentence = ['Gago', "ka", "pala"]
sentence_join = ' '.join(sentence)
print(sentence_join)
print(' '.join(sentence))

isabella = ['Lauren', 'Isabella', 'Babay']
print(' '.join(isabella))

