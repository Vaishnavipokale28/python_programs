x=input("Enter a character")
y=ord(x)
print(y)
if y>=65 and y<=90:
    print("Character is capital alphabet")
elif y>=97 and y<=122:
    print("character is small alphabet")
elif y>=48 and y<=57:
    print("character is digit")
else:
    print("character is special symbol")