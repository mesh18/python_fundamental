#passing a function as an argument
import functools

def my_function():
    print("Original function")

def wrapper(func):
    func()

wrapper(my_function)

"""        BASIC DECORATOR    """
def changecase(func):
    def myinner():
        return func().upper()
    
    return myinner()

@changecase
def New_function():
    return "Hello meshack"

print(New_function)

@changecase
def my_speed():
    return "Hey i am speeding"

print(my_speed)

"""        Arguments in the decoration function"""
def changename(func):   #decorator function
    def inner_function(name):
        return func(name).upper()  #function that performs the decoration
    return inner_function #retruns the decoration

@changename
def my_name(name):
    return  "hello "  + name

print(my_name("Meshack Magara"))

"""      Multiple decorator """
def change_case(func):
    def myinner():
        return func().upper()
    return myinner()
    

def add_greeting(func):
    def inner():
        return "Hello " + func() + " and have a good day"
    return inner()

@change_case
def new_function():
    return "tobias"

print(new_function)

