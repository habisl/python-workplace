"""
To create a generator, you define a function as you normally would but use the yield statement instead of return, 
indicating to the interpreter that this function should be treated as an iterator:
"""

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


val = countdown(5)

