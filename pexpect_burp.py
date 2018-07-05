# Script to install burpsuite in headless mode
# To replace bash echo

import sys, pexpect.popen_spawn, signal

if len(sys.argv) != 3:
    print('Usage: license-burp [yes/no] [license-file]')
    sys.exit(1)

if sys.argv[1] != 'yes':
    print('You must accept the license to use Burp')
    sys.exit(1)

license = open(sys.argv[2]).read()

base = "c:/Program Files/BurpSuitePro"
#child = pexpect.popen_spawn.PopenSpawn('%s/jre/bin/java -Djava.awt.headless=true -jar "%s/burpsuite_pro.jar"' % (base, base), encoding='cp437')
child = pexpect.popen_spawn.PopenSpawn('java -Djava.awt.headless=true -jar "./burp-rest-api-1.0.3.jar"')
#child.logfile = sys.stdout

child.expect('Do you accept the license agreement\\? \\(y/n\\)')
child.sendline('y')

child.expect('please paste your license key below.')
child.sendline(license)

child.expect('Enter preferred activation method')
child.sendline('o')

child.expect('Your license is successfully installed and activated.')
child.kill(signal.SIGTERM)
print('Your license is successfully installed and activated.')
