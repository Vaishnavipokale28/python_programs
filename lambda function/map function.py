#squares of numbers
list1=[90,28,41,31,51,81,80,87,9,68]
list2=list(map(lambda x: x*x,list1))
print(list2)
print("--------------------------------------------")

#taking multiple input in single line
s1=input("enter number seperated by ,")
print(s1)
arr=list(map(int,s1.split(',')))
print(arr)
print("---------------------------------------------")

#convert to upper case
list1=['hello','world','demo','string']
print(list1)
list2=list(map(lambda x:x.upper(),list1))
print(list2)