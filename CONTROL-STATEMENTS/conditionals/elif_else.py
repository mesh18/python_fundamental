name = "mel"

age = 19
country = "USA"

if age <= 20:
    print(f"{name} is at {age} years")
#we cant have a piece of code in between the conditions if and else statement they must be continuous
elif age <= 40:
    print(f" {name} is betewen 20 and 40 years")
elif age <= 60:
    print(f"{name} is between 40 and 60 years")
else:
   print(f"{name} is over 60 years")

   #using a boolean value

is_over_18 = age > 18
print(f"is over 18 : {is_over_18}")

if is_over_18 is True:
    print(F"{name} is over 18")


random_none = None
if random_none is not None:
    print("YEP is a not none value")

random_value = 1

if random_value:
    print("OVER THE BAR")
