num = int(input("Enter a number : "))
a = num%7
b = num%10
if a == 0 and b==5:
    print("no. is divisible by 7 and last digit is 5")
else:
    print("either no. is not divisible by 7 or the last digit is not 5")