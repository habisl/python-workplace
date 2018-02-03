# A good use of while loop

password=''
while password != 'mypass123':
  password=input("Enter password: ")
  if password == 'mypass123':
    print("You are logged in!")
  else:
      print("Sorry, try again")
