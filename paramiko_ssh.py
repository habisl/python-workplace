#This code is working fine after changing the ssh key
#workable code for ssh connection

import paramiko


k = paramiko.RSAKey.from_private_key_file("\\Desktop\\mykey_rsa")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
c.connect(hostname="192.168.2.0", username="root", pkey=k)
print("connected")
commands = ["ifconfig"]
for command in commands:
    #in Executing{},should be 0 inside
    print("Executing {0}".format(command))  
    stdin, stdout, stderr = c.exec_command(command)
    print(stdout.read())
    print("Errors")
    print(stderr.read())
c.close()
