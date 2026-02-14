#lamda function is a funtion that can take any number of arguments but return only one expression
"""          Example      """
x = lambda a : a +10
print(x(5))

#one  can add more than one arguments
y = lambda a,b : a * b
print(y(10,20))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))