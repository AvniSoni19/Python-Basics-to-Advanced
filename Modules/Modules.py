#Module is a function only, but stored in different file with (.py) extension

import math #Inbuilt modules access
print(dir(math))
print(math.sqrt(25))

#Making our own modules 
import calculate #Direct .py file access
print(dir(calculate))
print(calculate.add(5,112))

from calc.advanced import sqrt #Multiple folder access
print(sqrt.sqrt(25))

from calc import cal #Single folder access
print(cal.add(3,8))