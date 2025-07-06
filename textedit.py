# Open function to open the file "MyFile1.txt"
# (same directory) in read mode ("r")
# if the file is in a different directory provide the relative path
file1 = open("MyFile1.txt","r")
file_content = file1.read() # stores the entire file content of the file as a string into the file_content variable
file_lines = file1.readlines() # stores each line of the file as an element of a list

file1.close() # make sure to close the file before opening in different mode

file1_w = open("MyFile1.txt", "w") # deletes all contents of the file and opens it for write mode ("w")

L = ["Hello\n", "World\n"]

file1_w.write("Hello") # writes hello to the file without adding a new line
file1_w.write("Hello\n") # same as above but starts a new line
file1_w.writelines(L) # pass in a list of strings and python writes each element of the list as a new line

