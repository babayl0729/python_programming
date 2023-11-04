# clear - Remove all items from the list.
clear_list = [1,2,3,4,5]
print(clear_list)
clear_list.clear()
print(clear_list)

# pop - Remove the item at the given position 
# in the list and return it.
# If no index is specified, removes & returns last
# item in the list.
pop_list = ["ira", "ely", "son", "lee", "leo"]
print(pop_list)
pop_list.pop()
print(pop_list)
pop_list.pop(0) # will remove ira
print(pop_list)

# remove - Remove the first item from the list
# whose value is x.
# Throws a ValueError if the item is not found.
remove_list = ["QC", "QC", "MD", "DC", "AB", "AB", "CA", "UT"]
print(remove_list)
remove_list.remove("QC")
print(remove_list)
remove_list.remove("AB")
print(remove_list)
remove_list.remove("MA")
print(remove_list)

