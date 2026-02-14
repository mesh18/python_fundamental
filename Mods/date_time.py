import datetime
x = datetime.datetime.now()

print(x.day)
print(x.strftime("%c"))

y = datetime.datetime(2020,5,17)
print(y.strftime("%a"))