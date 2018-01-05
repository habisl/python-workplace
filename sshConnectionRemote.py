import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("\nConnecting")

ssh.connect('192.168.245.345', username='xyz', password='xyz')
print("\nConnected")

cmd = "powershell -InputFormat none -OutputFormat TEXT Get-VMHost"
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.readlines())
