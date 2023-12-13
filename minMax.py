# max - return the largest item in an iterable
# or the largest of two or more arguments.

# min - returns the smallest item in an iterable
# or the smallest of two or more arguments.

print(max(3,6,99,102))
print(max('d','h','z','q'))
print(max("hello world"))
print(min("hello world"))

# list min max
nums = [100,20,129,10]
print(max(nums))
print(min(nums))

# tuple min max
numtups = (200,3,1,292)
print(max(numtups))
print(min(numtups))

# min max of names lenght
names = ['Isabella','Jaiden','Zander','William','Turdy']
print(min(len(name) for name in names))

# to find the longest and shortest name
#Isabella
print(max(names, key=lambda n:len(n)))
# Turdy
print(min(names, key=lambda n:len(n)))

songs = [
    {"title":"happy birthday","playcount":1},
    {"title":"Survive","playcount":6},
    {"title":"YMCA","playcount":99},
    {"title":"Toxic","playcount":31}
]
# min max played song
#{'title': 'happy birthday', 'playcount': 1}
print(min(songs,key=lambda s:s['playcount']))
#{'title': 'YMCA', 'playcount': 99}
print(max(songs,key=lambda s:s['playcount']))
# to get just the title
print(max(songs,key=lambda s:s['playcount'])['title'])

