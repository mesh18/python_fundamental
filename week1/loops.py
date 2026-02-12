"""
  LOOPS AND CONTROL STATEMETS
"""
""" 1 WHILE LOOP """
#It requires a relevant varibles to be readyin order to index the the loop

index = 1
while index <= 10 :
    print(index)
    index = index + 1

    if index == 3:
        print("reached a certan level")
        break

print("printing the number for ten to one in reversed order")
reversed_index = 10
while reversed_index > 0:
    print("number :" , reversed_index)
    reversed_index = reversed_index - 1

    if reversed_index == 4:
        print("I skipped the number at this point during loooping")
        continue

"""        2. FOR LOOP  """
#For loop i smajorly used in iterating over a sequence of items such as tuple, list, dictionary, sets
for x in range(0,10):
    print("For-number : ",x) #printing numbers from 1-9

#to print numbers in a series of step and knowing the starting value and the closing value
print("Even value between 10 and 40 are :")
for y in range(30,40,2):
    print(y)

"""    We can use loops to iterate through a set of items in an array  """

fruits = {"MANGO","APPLES","ORANGES","PINEAPPLES","LEMONS","PAWPAW"} #this is a set
cars = ['volvo','mercedez','lamborghini','toyota','volkswagen'] #this is a list
schools = ("primary","secondary",'high-school','colleges','universities') #this is a tuple
students = {
    "name" : "Meshack Magara",
    "school":"Egerton University",
    "Age": 19,
    "Height":23.5
} # this is a dictionary

print("-------------list of fruits----------------------")
for item in fruits:
    print(f"Item : {item}")

print("---------list of cars----------------------------")
for car in cars:
    print(f"Car : " , car)

print("------------------list of schools levels--------------")
for level in schools:
    print(f"school-level : {level}")

print("---------------my personal details------------------------")
for attribute,details in students.items():
    print(attribute, " : ", details )


    """We can add break and continue statements inside the for loop """
for fruit in fruits:
    if fruit == "PINEAPPLES":
        print(f"{fruit} is my favourite fruit 💝💝")
        break
    
    if fruit == "MANGO":
        continue

"""The else in for loop specifies the block of code to be excecuted when the loop is finished"""
for car in cars:
    print(car)
else:
    print("The loop is finally finished ")

    #nested loops
 
for car in cars:
    for fruit in fruits:
        print(f"{car} : {fruit}")

"""A python program that sum the even numbers between 10 and 50 """
sum = 0
for number in range(10,50,2):
    sum = sum + number

print("The total sum between 10 and 50 is : ", sum)

"""A python program that asks the user for an integer input and prints the multilication table """

number = int(input("Enter the number you wish for the multiplication table for : "))
for i in range(0,11):
    print(f"{number} * {i} = {number * i}")

"""A python program that count positive numbers and negative numbers in a list """
numbers = [10,23,-12,34,-45,-90,-23,93]
positive_number = 0
negative_number = 0

for number in numbers:
    if number > 0:
        positive_number += 1
    else:
        if number < 0:
            negative_number +=1
    
print(f"positive_numbers are : {positive_number}")
print(f"Negative numbers are : {negative_number}")

"""FizzBuzz: Print numbers from 1 to 50 with conditions"""
print("\n--- FizzBuzz (1 to 50) ---")
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} : FizzBuzz")
    elif number % 3 == 0:
        print(f"{number} :Fizz")
    elif number % 5 == 0:
        print(f"{number} : Buzz")
    else:
        print(number)
    