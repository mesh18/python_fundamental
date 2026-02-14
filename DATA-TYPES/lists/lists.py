"""Creating a list to store multiple data all at once"""
example_list = [] #empty list
list_two = [1,2,3,4,5,6,7,8,9,10] #list containing only one data type
list_three = [1,"34.90",False,{1,2,3},["apple",'mango','oranges']] #llist containing different data types

"""  Accessing the elements in a list """
#accessing through indexing
print(list_two[1])

print(list_three[-1])
# slicing through the list
print(list_two[2:])

print(list_three[:-1])

"""  LIST METHODS"""
# Getting the length of the list
print(len(example_list))
print(len(list_two))
print(len(list_three))

#checking if  specific item in the list exists
if 1 in example_list:
    print("Yes 1 exists in the example_list")
else:
    print("1 does not exist in the list")    

if False in list_three:
    print("Yes the value False exists in the third list")

if 2 in list_two:
    print("2 exists in the list")
else:
    print(" 2 does not exist in the list")


""" MODIFYING THE LIST"""

#changing the value of a specific item at a specific index
fruits = ['oranges','mango','berries','ovacado']

fruits[1] = "Mango" #changed the first letter to capital letter
print(fruits)

fruits[-1] = "Blackcurrent" #changed the last value from avocado to blackcurrent
print(fruits)

fruits[-2] = "Apple" #changed the second last value from berries to apple
print(fruits)

"""   INSERTING AND ADDITITON OF ELEMTENTS INTO THE LIST """
#using isert method -- it insert the item at a specified index without replacing the existing values
fruits.insert(1,"Pineapple")
print(fruits)

fruits.insert(-1,"Berries")
print(fruits)

fruits.insert(0,"Banana")
print(fruits)

# ADDING ITEMS TO THE END OF THE LIST
fruits.append("Lemon") #adds lemon to the end of the list
print(fruits)

fruits.append("papaya")
print(fruits)

# Extending the list
fruits.extend(list_two) #adding other elements of the list to the current list
print(fruits)
print(len(fruits))

fruits.extend(list_three)
print(fruits)
print(len(fruits))


""" REMOVING ITEMS FROM THE LIST  """
# The remove() method item
fruits.remove(False)  #it is used to the specified value from the list
print(fruits)

fruits.remove("Apple")
print(fruits)

# The pop() method
fruits.pop(-1)  , """ the pop method removes at a specified index """
print(fruits)


fruits.pop(2)
print(fruits)

#clear method empties the whole list
fruits.clear() , """it clear the whole list but the lsit still remaind but has no content"""
print(fruits)

""" SORTNG OUT THE  LIST"""
numbers = [1,2,743,534,4,68,67,564,342,545,66,90]
thislist = ['orange','mango','pineapple','watermelon','grapes']

#sorting the list aplhanumarically
thislist.sort()  , """by default it sort in descending order"""
print(thislist)

numbers.sort(reverse = True) , """this sorts in ascending order"""
print(numbers)
