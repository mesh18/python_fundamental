""" TUPLES """
#this are unchangeable data set 
fruits = ("mango","apple","pineapple","orange")
print(fruits)


print(fruits[1]) #items can be accessed through  index

#you can also convert a list or any othe data set/type into a tuple
numbers = [1,2,4,5,67,6]
this_numbers = tuple(numbers)
print(this_numbers)

#you can also convert it back into a list of numbers
list_numbers = list(this_numbers)
set_fruits = set(fruits)
print(list_numbers)
print(set_fruits)

#you can also join tuples
number_fruits = fruits + this_numbers
print(number_fruits)
