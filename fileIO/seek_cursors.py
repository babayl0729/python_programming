# Cursor Movement
# Python reads files by using a cursor
# This is like the cursor you see when you're typing
# After a file is read, the cursor is at the end
# to move the cursor, use the seek method

file = open("story.txt")
print(file.read())
# "This short story is really short.\nNow it's a little longer\nThe end."
print(file.seek(0))
# "his short story is really short.\nNow it's a little longer\nThe end."
print(file.seek(1))
# readline() read the first line
# 'This short story is really short.\n'
print(file.readline())
# ['This short story is really short.\n', "Now it's a little longer\n", 'The end.']
print(file.readlines())
# Closing a file
# You can close a file with the close method
# You can check if a file is closed with the closed attribute
# Once closed, a file can't be read again
print(file.close())
# True 
print(file.closed)


