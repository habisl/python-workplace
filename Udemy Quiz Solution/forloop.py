"""
In one of the previous exercises we created the following function that gets Celsius degrees as input and returns Fahrenheit, or a message if the Celsius input value is less than -273.15.

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
Please implement a for  loop that iterates through the following temperatures  list temperatures=[10,-20,-289,100]  and calls the above c_to_f   function in each iteration. In other words, this time you are using the function to calculate a series of values instead of just one value. 

The expected output: 

50.0
-4.0
That temperature doesn't make sense!
212.0

"""

temperatures=[10,-20,-289,100]


def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))
