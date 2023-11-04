# List methods: append, extend, insert

friends = ["Joey", "Rey", "Lori"]

# append - Add an item to end of the list.
# you cannot do this in append - friends.append("Nancy", "Noyi")
friends.append("Nancy")

# extend - Add to the end of a list all values passed to extend.
friends.extend(["William", "Jaiden", "Zander", "Olive"])

# insert - Insert an item at given position
friends.insert(0, "Isabella")

for x in friends:
    print(x)

