import module
a=module.add(100,200)
b=module.sub(100,90)
print(a)
print(b)

print("-------------------------------------------")

import module as mm
a=mm.add(180,200)
b=mm.sub(40,20)
print(a)
print(b)

print("---------------------------------------------")

from module import add, sub
a=add(280,435)
b=sub(438,283)
print(a)
print(b)