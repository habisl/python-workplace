"""
Write a Python function, which does the following:

have input parameters: [name, age]
asks user input for favorite_colour
uses a tuple for constant (string) values
finds the current date and calculates a lucky number using formula
($yourage - $dayofmonth) mod $hour  #(mod = modulo)
returns a string
Hi, my name is $yourname, I'm $yourage years old, and I like $yourfavoritecolour.
Today is $thisdate. 
My lucky number is $luckynumber. 

Copy and modify the script in the previous assignment to use this function, and verify that the original script and modified script with the function work similarly. 

Add a documentation section to the beginning of the function:
"""

import datetime


input_name = input("Enter your name here: ")
input_age = input("Enter your age here :")
input_color = input("Enter your favorite color: ")
#put them into a list
list_entry = [input_name, input_age, input_color]
#conver list to tuple
data = tuple(list_entry)

def tutorial(*data):
    #passing the tuple as parameter
    print(data[0], data[1],data[2]) #print the name, age and
    now = datetime.datetime.now()

    # find the current date meaning the day

    print ("Current date (day) =  %s" % now.day)

    current_date = int(now.day)
    num_age = int(input_age)
    current_hour = int(now.hour)
    print("formatted age is: " , num_age, "formatted current date/day is :", current_date)

    lucky = num_age - current_date
    print ("lucky calc", lucky)
    lucky_num = lucky % current_hour

    print ("lucky number is : ", lucky_num)
    #return

#calling the function 
tutorial(*data)
