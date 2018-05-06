"""
getch() (gets a character from user input, 
no output - this is useful for password input) and 
getche() (also outputs to the screen)
"""

#import msvcrt
## ...
#char = msvcrt.getch()
##or, to display it on the screen
#char = msvcrt.getche()


import msvcrt
while True:
    pressedKey = msvcrt.getch()
    if pressedKey == 'q':    
       print "Q was pressed"
    elif pressedKey == 'x':    
       sys.exit()
    else:
       print "Key Pressed:" + str(pressedKey)
