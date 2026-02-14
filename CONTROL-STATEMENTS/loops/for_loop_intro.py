print("Hello")
i= 5

mylist = ['a','b','c','d','e','f','g']
second_list = ['def','fgh']

for value in mylist:
    print(value)
    for second_value in second_list:
        print(second_value)
        total_value = value + second_value
        print(total_value)



for i in range(0,10,2): #start,stop,step
    print(i)
"""The value of i gets overwritten"""
print(f"the last value of i is : {i}")

#using a dummy placeholder value
for _ in range(5):
    print("hello")

names = ["Ben","mel",'greg']
ages = [21,34,23]

for i in range(len(names)):
    name = names[i]
    age = ages[i]
    print(f"name : {name}  age : {age}")

#you can use the zip method to combine the two lists
for name,age in zip(names,ages):
    print(name,age)

zip_code = (name,age)


#the number of the variables you pass in the for loop must be  equal to the number of the lit passed to  the zip in the order
list_one = ["John",'Sam','kidd','Mel']
list_two = [12,24,45,64]
list_three = [89,94,96,88]

for name,age,score in zip(list_one,list_two,list_three):
    print(F"Name : {name} Age: {age} Score : {score}")

#trying to understand the role of zip() method
cars = {'Toyota','Mercedez','g-wagon'}
colours =  ('red','blue','yellow')

results = zip(cars,colours)
print(list(results))