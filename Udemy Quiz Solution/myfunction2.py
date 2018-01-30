# Function with conditionals

def age_foo(age):
  new_age = age + 50
  return new_age
age = float(input("Enter your age: "))

if age < 150:
 print (age_foo(age))
else:
print("How it is possible?")


'''
The function that was implemented in one of the previous exercises checks integer datatypes,
but not about floats. So, please expand the conditional block so that floats are counted too.
'''
def string_length(mystring):
     if type(mystring) == int:
         return "Sorry, integers don't have length"
     elif type(mystring) == float:
         return "Sorry, floats don't have length"
     else:
         return len(mystring)
