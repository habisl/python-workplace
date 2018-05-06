proc = subprocess.Popen(['/bin/ls', 'something'],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if line != '':
    do_something
  else:
    break
