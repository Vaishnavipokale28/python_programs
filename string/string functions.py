s1="Hello world"
print(s1)
#convert to lower case
print(s1.lower())
#convert to upper case
print(s1.upper())
#convert upper case to lower and vice versa
print(s1.swapcase())
#convert first letter to upper case
print(s1.title())

print("------------------------------------------------")

s1='hello world hello this is demo'
#count
x=s1.count('l')
print(x)
x=s1.count("hello")
print(x)
#endswith
print(s1.endswith('demo'))
print(s1.endswith('dem'))
#startswith
print(s1.startswith('he'))
print(s1.startswith(('ello')))

print('--------------------------------------------------')

s1="This is string.This is demo"
#find
x=s1.find('is')
print(x)
#rfind
x=s1.rfind('is')
print(x)
#index
x=s1.index('is')
print(x)
#rindex
x=s1.rindex('is')
print(x)

print('----------------------------------------------------')

s1="hello123"
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
s1="123"
print(s1.isdigit())
s1='hello'
print(s1.isupper())
print(s1.islower())
s1="\n \t"
print(s1.isspace())



