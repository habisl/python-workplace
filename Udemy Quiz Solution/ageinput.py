def age_foo(age):
  new_age = float(age) + 50 # Is work as a local variable
  return new_age

age = input("Enter your age: ")
print(age_foo(age)) # Calculates the age that user will define

# For Celsius to Farenheit. That would return 50.0 which means 10 degree Celsius is equal to 50 degree Fahrenheit.
def cel_to_fahr(c):
    f = c * 9/5 + 32
    return f
print(cel_to_fahr(10))

# A function that takes any string as argument and returns the length of that string.
def string_length(mystring):
    return len(mystring)
print(string_length("Hello"))


