print('*************************************')


"""
If you run a=2/0, your program will stop.
So we do error handling via this block:

try:
    (a piece of code that may stop the problem)
except:
    (if 'try' fails, your program will go to 'except')
else: - optional 
    (it's mutually exclusive with 'except', so it's executed if 'try' is executed)
finally: - optional
    (always !!! executed)
    
    
Note, that there are 20 errors that are prebuild in Python, like 'ZeroDivisionError' or 'Value type'.
But there is no need to precise the in 'except':

except ZeroDivisionError as error:
    or
except:

- both will work

"""

print('*************************************')



"""
You can have multiple 'except' but only one will be executed

"""


try:
    a=2/0
    print('Here is my a = ' + str(a))
except ZeroDivisionError as error:
    print(error)
    print('No way - ZeroDivisionError !')
except:
    print('Welcome to except: Smth went wrong')
finally:
    print('No matter what - Hello from finally block')


print('*************************************')

"""
Check how 'else' if working, change 'a' to 2/0

"""

try:
    a=2/4
    print('Here is my a = ' + str(a))
except:
    print('Welcome to EXCEPT from except&else: Smth went wrong')
else:
    print('Welcome to ELSE from except&else:we are good!')
finally:
    print('No matter what - Hello from finally block')



print('*************************************')


"""
One more exemple

"""

import math

x = int(input('Please enter a positive number:\n'))
try:
    print(f'Square Root of {x} is {math.sqrt(x)}')

except ValueError as error:
    print(error)
    print(f'You entered {x}, which is not a positive number.')

finally:
    print('Hello from FINALLY')

print('*************************************')

"""

And what if you want to raise an customised error, like no negative values allowed? 
Do it with 'Raise' !

"""

b = -1
if b < 0: raise Exception("Sorry, no numbers below zero")
