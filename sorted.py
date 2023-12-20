# sorted returns a new sorted list from 
# the items in iterable

numsort = [4,2,1,9]
# [1, 2, 4, 9]
print(sorted(numsort))

#reversing

#[9, 4, 2, 1]
print(sorted(numsort, reverse=True))

# sorted in tuple
numsort1 = (3,1,7,9,0,99,54)
print(sorted(numsort1))

#reversing
print(sorted(numsort1, reverse=True))

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color":"purple"},
    {"username": "bob123", "tweets": [], "num":10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
#print(sorted(users,key=len))
# sorted username
print(sorted(users,key=lambda user:user['username']))
# sorted tweets
print(sorted(users,key=lambda user:user['tweets']))
# reversing
print(sorted(users,key=lambda user:user['tweets'],reverse=True))

# sort playcount
songs = [
    {"title":"happy birthday","playcount":1},
    {"title":"Survive","playcount":6},
    {"title":"YMCA","playcount":99},
    {"title":"Toxic","playcount":31}
]
print(sorted(songs,key=lambda s:s['playcount']))
# reversing
print(sorted(songs,key=lambda s:s['playcount'],reverse=True))