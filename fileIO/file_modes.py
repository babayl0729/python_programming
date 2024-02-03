# modes for opening files
# r - read a file(no writing) this is the default
# w - write to a file(previous contents removed)
# a - append to a file(previous contents not removed)
# r+ - read and write to a file(writing based on cursor)

#appends 
with open("story.txt","a") as file:
    print(file.write("writing files is great\n"))
    print(file.write("Here's another line of text\n"))
    print(file.write("Closing now, goodbye!"))

# r+
# r+ will not create a file if it doesn't exist
with open("story.txt","r+") as file:
    file.write(":)")
    file.seek(10)
    file.write(":(")