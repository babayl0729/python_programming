# You can also use open to write to a file
# Need to specify the "w" flag as the second argument
# 

with open("story.txt","w") as file:
    print(file.write("writing files is great\n"))
    print(file.write("Here's another line of text\n"))
    print(file.write("Closing now, goodbye!"))

with open("lol.txt","w") as file:
    print(file.write("hah"*100))