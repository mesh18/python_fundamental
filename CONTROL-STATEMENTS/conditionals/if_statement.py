test_var = 0

if test_var <= 0:
    print("Yes it is")

temperature  = int(input( "Enter the temperature value : ") )
if temperature > 20:
    print("It is a hot day")

if temperature < 20:
    print("it is a cold day")

bill = int(input("Enter the bill you have for the end of the month : "))
if bill > 2000:
    bill *= 0.9

print(f"Your final bill is: {bill}")