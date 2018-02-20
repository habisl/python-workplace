# keeps asking for numbers until count numbers have been entered.
# Prints the average value.
# An integer was used to keep track of how many numbers, 
# but floating point numbers for the input of each number


sum = 0.0

print("This program will take several numbers then average them")
count = int(input("How many numbers would you like to average: "))
current_count = 0

while current_count < count:
    current_count = current_count + 1
    print("Number", current_count)
    number = float(input("Enter a number: "))
    sum = sum + number
    
print("The average was:", sum / count)
