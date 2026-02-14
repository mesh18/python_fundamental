#converting farenheit values to celcius values
def farenheit_to_celsius(farenheit):
    return (farenheit - 32 ) * 5/9

print(f"{farenheit_to_celsius(45) : 2f}")
print(farenheit_to_celsius(77))
print(farenheit_to_celsius(100))
print(farenheit_to_celsius(273))

#Return values
def greeting():
    return "hello from a function"

message = greeting()
print(message)

""" You can use the return value directly without initializing it to a variable"""

print(greeting())