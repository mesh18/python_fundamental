"""Python function arguments"""
#a function with one argument
def my_function(fname):
    print(fname + " " + "Willis")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# parameter values and arguments passed into   function
def my_name(fname,lname):
    print(f"My name is {fname} {lname}")

my_name("Meshack","Magara") # a function must be called with the correct number of arguments

#Default parameter values
def default_parameters(name = "\'unknown\'"):
    print(f"Hello {name}")

def default_country(country = "kenya"):
    print(f"I am from {country}")


default_parameters()
default_parameters("jackline")
default_country()
default_country("turkey")

#keyword arguments
def my_pet(animal, name):
    print(f" i have a {animal}")
    print(f"the name of my {animal} is {name}")

my_pet(animal = "Dog" , name = "Jowi") #calling a function with the key word arguments

def my_name(name):
    print("My name is : " , name)

my_name(name = "john kiamenyu")

#you can mix both positional and key-word arguments in a function call
# example :

def my_car(name,color,year) :
    print("Name : " , name ,"\n", "COLOR : " , color, "\n" , 'Year :' , year)

my_car('Toyota',color = 'pink',year = 2030)

#you can also send in any data type 
def fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ['mango','cherry','melon','oranges']
fruits(my_fruits)

def sum(a,b):
    return a+b #only returns the value of summation nothing else
print(sum(10,20))

#a function can return any data type
def cereals():
    return ['maize','banana','lemon']

food = cereals()
print(food[2])

#we can specify a function to have only positional arguments
def function(name,age,year):
    print("hello ", name)
    print("You are ", age, " years old")
    print("You were born in : ", year)

function('meshack',45,year = 1990)

#to specify that a function can only have key word arguments we use ,*
def new_function(*,name,age,year):
    print("hello ", name)
    print("You are ", age, " years old")
    print("You were born in : ", year)

new_function(name = 'james',age = 43,year = 1923)

# we can combine both the positional arguments together with the keyword only arguments
def newer_function(name,school,/,*,age,year):
    print("hello ", name)
    print("You are learning in : ", school)
    print("You are ", age, " years old")
    print("You were born in : ", year)

newer_function('Henry','Egerton university',age = 23, year = 2009)

#python *args and **kwargs
def schools(*name): 
    print(name[2])

schools('were','jsnfns','reusbs')

def my_school(**name):
    print(name["lname"])

my_school(fname = 'james', lname = 'caleb')

