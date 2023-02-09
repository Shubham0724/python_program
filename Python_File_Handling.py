file = open("someText.txt")
print(file.read())

#Read/Write Files

#A. Create a File:
file = open("Text.txt", "x")


#B. Write onto a File:
file = open("Text.txt", "w")
file.write("This is an example of file creation.")
file.close

#C. Read a File:
file = open("Text2.txt", "r")
print(file.read())
file.close

#D. Append a File:
file = open("newText.txt", "a")
file.write("This is an example of file appending.")
file.close

