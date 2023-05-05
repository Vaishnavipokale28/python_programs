print("----creating simple module------")
import module
a=module.add(100,200)
b=module.sub(100,90)
print(a)
print(b)

print("----rename imported module-----")

import module as mm
a=mm.add(180,200)
b=mm.sub(40,20)
print(a)
print(b)

print("-----importing only function from module-----")

from module import add, sub
a=add(280,435)
b=sub(438,283)
print(a)
print(b)

print("---importing everything from the module---")
from math import*
from module import*
a=add(100,200)
print(a)
b=sub(50,30)
print(b)
c=pow(10,2)
print(c)

print('---find module----')

from math import*
from module import*
import sys
arr=sys.path
for p in arr:
    print(p)