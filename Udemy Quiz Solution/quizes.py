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

'''
Now, the lowest possible temperature that physical matter can reach is -273.15 °C. 
With that in mind, please improve the function by making it print out a message in case a number 
lower than -273.15 is passed as input when calling the function.
'''
def c_to_f(c):    
    if c< -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f=c*9/5+32        
        return f
print(c_to_f(-273.4))
# A function that takes any string as argument and returns the length of that string.
def string_length(mystring):
    return len(mystring)
print(string_length("Hello"))

#What would the following code output?

mynumber  = 5.0
if type(mynumber) == int:
    print("It's an integer")
elif type(mynumber) == float: # Since 5.0 is a float datatype, the statement under elif would be executed.
    print("It's a float")
else:
    print("It's not a number")


