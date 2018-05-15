# Program that input username and password to register
# Atleast 1 letter between [a-z] and [A-Z]
# Atleast 1 number between [0-9]
# Atleast one chracter from [#%@!]

low_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upp_case=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=[0,1,2,3,4,5,6,7,8,9]
spc_char=['#', '%', '@', '!']

def sucess():
  print("Sucess!" + username + "  your password has been created")
# not ready yet
def validator():
  if(l>6 and l<12):
    
    for i in password:
      if i in low_case and num and spc_char and upp_case:
             sucess()
             break
  
  else:
    print("Ops! Your password doesn't fulfill minimum requirments")
      
username=input("Enter your username: ")
password=input("Create the password: ")
l=len(password)
validator()
