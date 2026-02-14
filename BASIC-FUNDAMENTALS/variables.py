#Declaring and initializing a variable
word = "hello world"

print(word)

#declaring and assigning the variable to another variable
hello_world_copy = word
print(hello_world_copy)

#strings
name = '"Meshack Magara"'

print(f"name : {name}")

#spacing out charactters in string
pr = 'isn\'t'
print(pr)

#separating the string from the quotation marks
name_sake = "\" Meshack magara\""
print(name_sake) 

#joining strings
word1 = "Hello"

greeting = word1 + " " + name
print(greeting)

#accessing the elements of a string
#accessing the first element of a string
print(f"letter : {word1[0]}")
#licing the letters
print(f"{greeting[3:6]}")

#function to give the index of an element
letter_h = word1.index("l")
print(f"index : {letter_h}")

#changing the string to uppercase
new_greeting = greeting.upper()
print(f" new greeting =  {new_greeting}")

x = "I\'M out"[0:3] + "in"
print(f"X : {x}")

toomanyspaces = "spaces "[0:-1] * 3
print(toomanyspaces)