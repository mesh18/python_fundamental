"""A program that takes in integer input and prints 
   --whether the input is odd, even or zere
   --whether the input i positive, negative
   --wheter the input is a multiple of three and five

"""

number = int(input("Enter the number you wish to check for the conditions : "))

 #checking if the number is zero, negative or positive
if number == 0:
    print("The number is zero ")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")

#checking if the number is odd or even
if number % 2 == 0:
    print("The number is an even number ")
else:
    print("The number is an odd number ")

#checking for the multiple of 3  and 5
if number % 3 == 0 and number % 5 == 0:
    print("The number is a multiple of both 3 and 5 ")
else:
    print("The number is not a multiple of both 3 and 5")


"""PROBLEM SET 2 : 
   GRADE ANALYZER

"""

def analyze_grade(score):
    if score >= 80 and score <= 100:
        print(f"GRADE : 'A'")
    elif score >= 70 and score < 80:
        print(f"GRADE : 'B'")
    elif score >= 60 and score < 70:
        print(f"GRADE : 'C'")
    elif score >= 50 and score < 60:
        print(f"GRADE : 'D'")
    elif score >= 40 and score < 50:
        print(f"GRADE : 'E'")
    else:
        print(f"GRADE : 'F'")
    
score = float(input("Enter your score : "))
analyze_grade(score)

"""PROBLEM 3: TRIANGLE TYPE DETECTOR """

def triangle_checker(a,b,c):
    if a == 0 or b == 0 or c == 0:
        print("An Invalid triangle")
    else:
      if a == b and b == c:
         print("This is an Equilateral Triangle")
      elif a == b or b == c or c == a :
        print("This is an Isosceles Triangle")
      elif a != b and a != c and b != c:
        print("This is a scalene Triangle ")
    

side_one = float(input("Enter the first side of the triangle : "))
side_two = float(input("Enter the second side of the triangle : "))
side_three = float(input("Enter the third side of the triangle : "))

triangle_checker(side_one,side_two,side_three)

" writing a python function that return the sum of digits of a number without converting it to strings  "
def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    
    total = 0 
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(100))