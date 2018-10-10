# program for listing file from system

import os, glob

os.chdir("C:\Users\Habibul\Desktop\Python Masterclass\Projects")
for file in glob.glob("*.py"):
  print(file)
