"""         VARIABLES """
import datetime
"""Types of basic data types """
# integers
# floats
# boolean
# strings
# none

name = "Meshack Magara"
age = 12 
is_sick = False
degree = None

print("my name is :", name)
print("i am " , age , " years old")
print("Am i sick : ",  is_sick)
print("Do you have a degree : ",degree)

"""  type conversion in python """
x = "19"
y = int(x)

a = 30
b = str(a)

c = "50"
d = float(c)

print(y,b,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(x))
print(type(y))

your_year = int(input("Enter the year you were currently born : "))

current_year = datetime.datetime.now().year

age = current_year - your_year

print(f"you were born in {your_year} and you are currently {age} years old ")

length = float(input("Enter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle : "))
area = int(length * width)

print(f"A rectangle of length {length} cm and width {width} cm has an area of {area} cm^2 ")

"""a program that asks the user for the name, age and height"""
names = input("Full name : ")
Age = int(input("Your Age: "))
height = float(input("Your height in metres"))

print("-------------------------------------------------------")
print("------------MY DETAILS-------------------------")
print("NAME : " ,name)
print("Age next year : " ,(age + 1))
print("Height in cm : ",(height * 100))
print("--------------------------------------------------------")