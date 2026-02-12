# Take two numbers and find their sum, difference , product and quotient
a = int(input("enter you first number : "))
b  = int(input("Enter your second number : "))
"""
        ARITHMETIC OPERATORS

"""
quotient = a / b
sum = a + b
product = a * b
difference = a - b

print("QUOTIENT : ", quotient)
print(f"SUM : {sum}")
print(f"PRODUCT : {product}")
print(f"DIFFERENCE : {difference}")

""" 
    COMPARISON OPERATORS

"""

if a > b :
    print(f"{a} is greater than {b}")
elif b > a:
 print(f"{b} is greater than {a}")
else :
   print("Both numbers are equal")

"""
       LOGICAL OPERATORS

"""
# a program that grants access to a peron who has more than 18 years and has id
age = int(input("Enter your current age :"))
has_id = bool(input("Do you have an id:(True or False) : "))

if age >= 18 and has_id == True:
   print("You are allowed to enter the club and have fun 😂😂😂")
else:
   print("You are not allowed to enter into the club and have fun because you are underage 😭😭😭😭")