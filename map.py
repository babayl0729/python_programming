# map - a standard function that accepts at least two
# arguments, a function and an "iterable"
# iterable - something that can be iterated over(lists,
# strings, dictionaries, sets, tuples)
# runs the lambda for each value in the iterable and
# returns a map object which can be converted into
# another data structure.

l = [1,2,3,4]
doubles = list(map(lambda x:x*2,l))
# [2, 4, 6, 8]
print(doubles)

names = [
    {'first':'Rusty','last':'Sponge'},
    {'first':'Isabella','last':'Babay'},
    {'first':'Spot','last':'Spotter'}
]
first_names = list(map(lambda x: x['first'],names))
# ['Rusty', 'Isabella', 'Spot']
print(first_names)

