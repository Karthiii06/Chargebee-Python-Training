#object oriented programming language

#classes, object

class first:
    a=78

    def method1(self):
        print("m1")
#object
o1=first()
print(o1.a)

o1.a=80
print(o1.a)
o1.method1()

#inheritance
class second(first):
    b=45
    def method2(self):
        print("m2")
s1=second()
print(s1.b)
print(s1.a)

#print(o1.b)"""error

#modules

import cal
cal.add(13,2)

import cal as m
m.sub(22,12)

from cal import div
div(5,15)

from cal import *
add(64,46)
sub(69,6)
mul(9,9)
div(6,3)
