x=int(input("Enter any number"))
sum=0
num=1
while  num<=x:
    if (num %2 !=0):
        print(num)
        sum=sum+num
    num=num+1

print("The sum of even numbers from 1 to N ", sum)