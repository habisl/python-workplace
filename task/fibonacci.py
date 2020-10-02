
# -----------------------------------------------------------
# Python script which prints Febonacchi series based on given 
# range of a positive integer
# 
# -----------------------------------------------------------

# First check if the input value is positive integer or not
num = None 
while type(num) is not int: 
   try: 
      num = input("Please enter an integer: ") 
      num = int(num) 
      print("You entered: %d" % num) 
   except ValueError: 
      print("%s is not an integer.\n" % num)
       
a,b = 0,1
for i in range(0,num):
  print(a)
  a,b = b, a+b
