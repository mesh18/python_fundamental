try:
    print(x)
    quotient = 30/0
    print(quotient)
except NameError:
 print("an error of naming has occurred")
except:
   print("something wwent wrong")

try:
   print("hello")
except:
   print("somethindg went wrong")
else:
   print("Nothing went wrong") #lets you print the block of code if no error occurred
finally:
   print("the try-except block is finished")

"""      raising an error"""
try:
   x = -1
   if x < 0:
      raise Exception("Sorry no number below zero is allowed")
except:
   print("nothing went wrong in the process")

y = -2
if y < 0:
   raise Exception("Sorry number above zero not  allowed")

"""      specifying the type of error you want to  be raised"""

a =  "hello"
if not type(a) is int:
   raise TypeError("only integers are allowed")
