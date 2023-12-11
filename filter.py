# filter - there is a lambda for each value in the
# iterable. 
# Returns filter object which can be converted into
# other iterables.
# The object contains only the values that return
# true to the lambda

l = [1,2,3,4]
evens = list(filter(lambda x:x%2 == 0,l))
# [2, 4]
print(evens)

# return names that starts in 'I'
names = ['isabella', 'ian', 'arnold', 'ivan']
# ['isabella', 'ian', 'ivan']
i_names = filter(lambda n:n[0]=='i',names)
print(list(i_names))

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]
# [
# {'username': 'jeff', 'tweets': []}, 
# {'username': 'bob123', 'tweets': []}, 
# {'username': 'guitar_gal', 'tweets': []}
# ]
inactive_users = list(filter(lambda u:len(u['tweets'])==0,users))
print(inactive_users)

# Combining filter and map
usernames = list(map(lambda user:user['username'].upper(),
        filter(lambda u:not u['tweets'],users)))
# ['JEFF', 'BOB123', 'GUITAR_GAL']
print(usernames)

# List Comprehension
inactive_users1 = [user["username"].upper() for user in users if not user['tweets']]
print(inactive_users1)

inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)

# Exercise
def remove_negatives(list1 = [-1,3,4,-99]):
    list2 = list(filter(lambda x:x>=0,list1))
    return list2
print(remove_negatives())