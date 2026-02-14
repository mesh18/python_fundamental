# Looping through lists
""" you may loop through list items using for loop"""
fruits = []
fruits.append("Mango")
fruits.append("Oranges")
fruits.append("Pineapple")
fruits.append("Berries")
fruits.append("Apple")
fruits.append("Lemon")
fruits.append("Watermelon")

print(fruits)

for fruit in fruits:
    print(fruit, end = " ") , """it will print all the list items in one line """

"""you can also loop through thr list items by referring to their index numbers"""
for i in range(len(fruits)):
    print(fruits[i])


#looping using list comression
print("pritning the list using list compression")
[print(x) for x in fruits]