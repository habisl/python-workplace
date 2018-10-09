# Printing Febonacchi series based on given range

n = int(input("How many numbers you want in this series:"))

# Initializing the starting numbers
first_num = 0
second_num = 1

for i in range(n):
  print(first_num)
  temp=first_num
  first_num=second_num
  second_num= temp+second_num
  
# Output will be: 
# How many numbers you want in this series: 6
# 0
# 1
# 1
# 2
# 3
# 5
