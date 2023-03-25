x = int(input("enter a number:"))
total = 0
num = 1

while num <= x:
    if (num % 2 == 0):
        print(num)
        total = total + num
    num = num + 1

print("The sum of even numbers from 1 to N ", total)

