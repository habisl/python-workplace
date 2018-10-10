# Lists

print("Printing list:")
my_list = [10,20,30,40,50]
for i in my_list:
  print(i)

# Tuples
print("Printing from tuple:")
my_tup = (1,2,3,4,5,6,7,8,9,10)
for i in my_tup:
  print(i)

# Dict
print("Printing from Dict:")
my_dict = {'name':'Habibul', 'age':'26', 'occupation':'Engineer'}
for key, val in my_dict.items():
  print("My {} is {}".format(key,val))

# Set
print("Printing from set:")
my_set = {10,20,30,40,50,10,20,30,40,50}
for i in my_set:
  print(i)
