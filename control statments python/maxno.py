a = int(input("Enter a number = "))
b = int(input("Enter a number = "))
c = int(input("Enter a number = "))
if (a>b and a>c):
    print(a,"First number is the Maximum")
elif (b>c):
    print(b,"Second number is the Maximum")
else:
    print(c,"Third number is the Maximum")