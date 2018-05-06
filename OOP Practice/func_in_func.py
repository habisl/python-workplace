# Functions inside Functions
# Decorators example 
def f():
    
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
        
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

    
f()
