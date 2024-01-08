# We can use a for loop to 
# iterate over a tuple just
# like a list.

names = ('Isabella', 'Jaiden', 'Zander', 'William')
for name in names:
    print(name)

months = ('Jan', 'Feb', 'Mar', 'April', 'May', 'June',
          'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

for month in months:
    print(month)

i = len(months)-1
while i >= 0:
    print(months[i])
    i -= 1

# count - returns the number of a times a value
# appears in a tuple.

x = (1,2,3,3,3)
print(x.count(1)) # 1
print(x.count(3)) # 3

# index - returns the index at which a value
# is found in a tuple.

x = (1,2,3,3,3)
print(x.index(1)) # 0
print(x.index(3)) # 2 - only the first matching index is returned
#x.index(5) # ValueError: tuple.index(x): x not in tuple

# you can also use slices

nums = (1,2,3,(4,5),6,7)
print(nums[0:])
print(nums[0:4])
print(nums[0:4:2])

