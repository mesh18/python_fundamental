# creating a dictionary
my_dictionary = {}

print(my_dictionary)

my_dictionary.setdefault("student",True) #etting a default value of the dictioanry
print(my_dictionary)

#creating a list with key-value pair
student_profile = {
    "Name" : "Kingstone",
    "Age":20,
    "DOB":2006,
    "class":"Computer Science"
}

""" Accessing items from the list"""
"getting the name of the student"
print(student_profile.get("Name"))

#getting the age of the student
print(student_profile.get("Age"))

#add items to the dictionary using the key method
student_profile["House"] = "Naivasha"
print(student_profile)

student_profile["Grade"] = "A plain"
print(student_profile)

# We can also overwrite the value of a certain kkey
student_profile["DOB"] = 2007
print(student_profile)

student_profile["Age"] = 19
print(student_profile)

student_profile["Grade"] = "B Plain"
print(student_profile)

"""Using variable to access the value in the dictionary"""
my_name = "Name"
print(student_profile[my_name])


my_course = "class"
print(student_profile[my_course])

del my_dictionary["student"]
print(my_dictionary)
