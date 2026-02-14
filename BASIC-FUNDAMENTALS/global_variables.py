#global variables are defined outside all other functions and classes
value = 30 #this global variable can be read inside any function

def find_value():
    age = value - 10 #the value variable can be accessible inside the function
    print("my age is : ", age)

find_value()

#if you want to change the global variables inside the function:
def change_value():
    global value #declare it first as a global variable 
    value = value + 10
    print(value)

change_value()
print(value) #the value is forty because i have already changed the value

