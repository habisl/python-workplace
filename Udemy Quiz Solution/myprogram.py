def age_foo(age):
  new_age = float(age) + 50 # Is work as a local variable
  return new_age

age = input("Enter your age: ")
print(age_foo(age)) # Calculates the age that user will define
