#find even numbers
list1=[1,6,34,98,74,99,56,38,93,62,73,75,90,12,67,32]
list2=list(filter(lambda x: x%2==0,list1))
print(list2)
print("-----------------------------------------------------")

#find numbers from list which are divisible by 7
list1=[1,7,23,14,56,21,28,65,35,42,88,79,49,56,63,70,55,77]
list2=list(filter(lambda x: x%7==0,list1))
print(list2)