'''The program allows computer user
to remind take a break in every 2 hours in the current time

'''

import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on: " + time.ctime())
while (break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=f_kA3IbS4m4")
    break_count = break_count + 1