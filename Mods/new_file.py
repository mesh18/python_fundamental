#to use a module we need to import the module
import mymodule
mymodule.greeting("Jacob Halima")

print(mymodule.age)

mymodule.details(mymodule.student)

functions = dir(mymodule)
x = len(functions)
print(functions[-4:])