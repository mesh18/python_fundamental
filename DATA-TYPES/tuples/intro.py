# CREATING A TUPLE
tuple_1 = ("apple",1,2,3,'mango','pineapple',34.56,{90,34,98},['oranges','lemom']) 

print(tuple_1)

list_one = ["cars",'vans','nissans','buses']
converted_tuple = tuple(list_one) #converted the list to tuple using a tuple() constructor
print(converted_tuple)

"   ACCESSING TUPLE ITEMS  "
#Accessing items inside the tuple using index
print(converted_tuple[2])

print(tuple_1[0:3])
