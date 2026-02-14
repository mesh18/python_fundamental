#using the get method
my_dictionary = {
    "Name" : "Kingstone",
    "Age":20,
    "DOB":2006,
    "class":"Computer Science"
}

print(my_dictionary.get("Name")) #returns the value of the name key
print(my_dictionary.get("age",19)) #returns 19 because there is no key "age" that has a value
print(my_dictionary.get("DOB","NONE")) #returns 2006 because ther is a value attached to DOB

"""checing if a value exists in a certain dictionary"""
if "name" in my_dictionary:
    print("Yes  the key exist in the dictionary")
else:
    print("NO it does not exist in the dictionary ")

if 20 in my_dictionary:
    print("TRUE")
else:
    print("false")

keys = my_dictionary.keys() #used to get the keys of  the dictionary
print(keys)

values = my_dictionary.values()
print(values)

my_dictionary["Class"] = "Electrical engineering"
print(my_dictionary)

"""updating method"""
my_dictionary.update({"Name" : "Kingstone"})
print(my_dictionary)

my_dictionary.update({"DOB" : 2000})
print(my_dictionary)

my_dictionary.update({"House" : "Naivasha"})
print(my_dictionary)