'''
To change the behavior of len(), 
we need to define the __len__() special method in our class. 
Whenever we pass an object of our class to len(), 
our custom definition of __len__() will be used to obtain the result. 
Here is the pythonic way of executing that.
'''

# Pythonic way

class Order:
     def __init__(self, cart, customer):
         self.cart = list(cart)
         self.customer = customer

     def __len__(self):
         return len(self.cart)


# >>> order = Order(['banana', 'apple', 'mango'], 'Real Python')
# >>> len(order)
# 3

'''
As we can see, we can now use len() to directly obtain the length of the cart. 
Moreover, it makes more intuitive sense to say “length of order” 
rather than calling something like order.
get_cart_len(). 
The call is both Pythonic and more intuitive. 
When you don’t have the __len__() method defined but still call len() on your object, you get a TypeError:
'''
