# reversed - return a reverse iterator
for x in reversed("hello world"):
    print(x)

# remember you can used slice to reverse a string
print("hello"[::-1])

# complex way to reversed a string 
# turn it to a list
print(list(reversed("hello")))

# to join it back together
print(''.join(list(reversed("hello"))))

# using reverse in range
for x in reversed(range(0,10)):
    print(x)