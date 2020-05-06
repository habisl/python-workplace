>>> first = 'James'
>>> last = 'Bond'
>>> age = 90
>>> message = 'No, Mr. %s, I expect you to die' % last
>>> print(message)
No, Mr. Bond, I expect you to die
>>> print('The name is %s, %s %s' % (last, first, last))
The names is Bond, James Bond
>>> print('Sean Connery is now %d years old' % age)
Sean Connery is now 90 years old
>>> print('pi: %f \nshort pi %0.2f' % (math.pi, math.pi))
pi: 3.141593
short pi 3.14
>>> message = f'No, Mr. {last}, I expect you to die'
>>> print(message)
No, Mr. Bond, I expect you to die
>>> print(f'The name is {last}, {first} {last}')
The name is Bond, James Bond
>>> print(f"Sean's age times pi is {age*math.pi}")
Sean's age times pi is 282.7433388230814
>>> print(f"Sean's age times pi is {age*math.pi:.2f}")
Sean's age times pi is 282.74
