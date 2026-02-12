"      LISTS  "
""" 
   1. Creating a list and returning the length of the string
"""
fruits = ["MANGO","APPLES","ORANGES","PINEAPPLES","LEMONS","PAWPAW"]
list_length = len(fruits)
print(f"The length of the list is {list_length}")

#to check if the item belongs in the list we use the in keyword
users_choice = input("Enter a type of fruit you think is in the list: ")
if users_choice in fruits:
   print(f"YESS😊😊, {users_choice} does exist in the list")
else:
   print("oops!!! not found in the list ")

# If you want to change the value of an item in the list
fruits[3] = "PINEAPPLE"
print("New list with change value include : ")
print(fruits)
""" You can also change a range of items in a list  """
fruits[1:3] = ["APPLE","ORANGE"]
print("Changed a range of items in the list: ")
print(fruits)

""" You can also insert an item into the list  """
fruits.insert(3,"WATERMELON")
print(fruits)

"""To add an item at the end of the list we use the append() function """
fruits.append("BERRIES") #berries is added at the last index
print(fruits)

"""Appending a list of items from another list we use extend() method """
tropical = ["BANANA","CUCUMBER","PASSION"]
fruits.extend(tropical)  #it doesn't necessarily have to be a list it can be a set or tuple
print(fruits)
print(tropical)

""" Removing items from the list we can use two method ( remove() method and the pop() method)"""
#  The remove() method specifies the item to be removed
fruits.remove("BERRIES")
print(fruits)
fruits.remove("PASSION")
print(fruits)

#   The pop()method removes at a specified index 
fruits.pop(3)
print(fruits)
print("watermelon was popped ")

#  The clear() method removes all the items in the list
tropical.clear()
print(tropical)

""" SORTING A LIST """
#   One can sort a list in ascending order 
fruits.sort() #sorts the list in ascending by default
print("A new list that is sorted in ascending order is : ")
print(fruits)

#  One can also sort the list in descending order
fruits.sort(reverse = True)
print("A new list sorted in descending order is : ")
print(fruits)

# if you want a case sensitive case sensitive sort function we use sort(str.lower)

""" COPYING A LIST """
# we use a function copy()
good_fruits = fruits.copy()
print(good_fruits)

""" LOOPING USING LIST COMPRESSION """
[print(f"fruit : {x} ") for x in fruits]



""" CHALLENGES OF THE LISTS """
numbers = [1,2,3,4,5]
length = len(numbers)
print(numbers[0],numbers[length-1]) #printing the first and the last element in the listore

favourite_foods = ['Chapati',"cakes","Juices","Fruits","Mango"]
print(f"the lenght of my favourite food list is : {len(favourite_foods)} and my third best food is {favourite_foods[2]}")

names = ["John", "Mary", "Paul", "Anna"]

for i in range(len(names)):
   if i == 2:
      names[i] = "Peter"

print(f"Updated list : {names}")
numbers.append(100)
numbers.insert(2,15)
numbers.remove(15)
print(numbers)

sum = 0
for number in numbers:
   sum+=number
print("The total sum in the list of numbers is: ",sum)

even_numbers = 0
for number in numbers:
   if number % 2 == 0:
      even_numbers += 1
   
print("Total even numbers in the list are : ", even_numbers)

#reversing a list without using the reverse() method
items = [10,20,30,40,50]
item_length = len(items)

while item_length > 0:
   print(items[item_length-1])
   item_length = item_length - 1

#finding the largest and the smallest number in the list
largest_number = items[0]
smallest_number = items[0]

for item in items:
   if item > largest_number:
      largest_number = item
   else:
      if item < smallest_number:
         smallest_number = item

print("The smalest number in the list is : ", smallest_number)
print("The largest number in the list is : ",largest_number)

#Writing a program that removes duplicates in the list
data = [1,1,2,3,4,4,5,6,6,7,8,9,10,4,3] #ithout converting to sets

unique_numbers = []
for num in data:
   if num not in unique_numbers:
      unique_numbers.append(num)

print(unique_numbers)
second_data = [9,1,2,3,4,2,3,5,6,4,7,4,9]
i = 0
while i < len(second_data):
   if second_data[i] in second_data[:i]:
      second_data.pop(i)
   else:
      i += 1

print(second_data)

"""A program that merges to list and removes duplicate """
second_data.extend(unique_numbers)
print(second_data)

while i < len(second_data):
   if second_data[i] in second_data[:i]:
      second_data.pop(second_data[i])
   else:
      i += 1

print(second_data)

