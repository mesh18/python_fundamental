count = 0
while count<10:
    print(count)
    count += 1

count_1 = 0
while count_1< 10:
    count_1 += 1
    if count_1 % 2 == 0 :
        continue
    print("odd numbers : ", count_1)

count_two = 20
while count_two >= 0:
    count_two -= 1
    if count_two % 2 == 1:
        continue
    print(count_two)

x = 0
while x < 4:
    x += 1
    print(x)
    break