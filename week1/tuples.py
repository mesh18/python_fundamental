"""   TUPLES   """
#create a tuple and print out the second element and the fourth element
numbers = (10,20,30,40,50,20,40,60,20,10,20,80,90,10,20,10,100,20,110,120,10)

print(f"The second element in the tuple is : {numbers[1]}")
print(f"The fourth number in the tuple is : {numbers[3]}")

#counting how many time 10 and 20 appear in the tuple
is_20_and_10 = 0
for number in numbers:
    if number == 20 or number  == 10:
        is_20_and_10 += 1

print(f"20 and 10 appears  {is_20_and_10} times in the tuple")

#convert a tuple and add an element into it 
data = ("mango","apple","orange","lemon")
data = list(data) #changes to list

data.append("Watermelon")
data.insert(1,"coconut")

print(f"Tuple after converting and adding elements into it is: {data}")

#swapping two variables using tuples
a = 10
b = 20

data = (a,b)
a = data[1]
b = data[0]
print(f" a : {a} and b :{b} ")

#finding the student with the highest score in the to dimensional array tuple
students = (("John",80),("Mary",60),("Jacob",100),("Jackline",50))

top_student = students[0]

for student in students:
    if student[1] > top_student[1]:
        top_student = student

print(f"The highest score in the tuples is : {top_student}")
     

