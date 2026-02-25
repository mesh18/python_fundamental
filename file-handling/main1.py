f = open("test_file.txt",'w')

f.write("This is a new file created\n")


f.close()

f = open("test_file.txt",'a')
f.write("writing the second line of the file\n")
f.write("THis is the third time i am writing the file\n")
f.close()

f = open("test_file.txt")
file_contents = f.read()
print(file_contents)
f.close()

f = open("file_one.txt","w")
f.write("welcome to the second file created \n")
f.write("i love using python in coding to open and close files \n ")
f.close()

s = open("file_one.txt","r")

for line in s.readlines():
    print(line," \n")

s.close()

""" REMOVING THE FILE FROM THE DIRECTORY """
#importing the os module 
import os

#checking if the file has a path in the os
if os.path.exists("file_one.txt"):
    os.remove("file_one.txt")
    print("FILE DELETED SUCCESSFULLY ")

else:
    print("The file does not exist")
