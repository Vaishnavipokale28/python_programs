x=int(input("Enter three digit number"))
a=x//100
b=x%100
c=b//10
d=b%10
y=d*100+c*10+a
print(y)