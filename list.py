# Accessing Values in a List

friends = ["Ashley","Matt","Michael"]
print(friends[0])
print(friends[1])
print(friends[2])

# len is leght
print(len(friends))

# number to index backwards
print(friends[-1]) # Michael
print(friends[-3]) # Ashley
print(friends[-4]) # IndexError

# Check if a value is in a List
"Ashley" in  friends # True
"Larry" in friends # False

# Iterating over Lists (for and while loops)
for friend in friends:
    print(friend)

i = 0
while i < len(friends):
    print(friends[i])
    i+=1
