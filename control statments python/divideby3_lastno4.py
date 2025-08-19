num = int(input("Enter a number : "))
a = num%3
b = num%10
if a == 0 and b==4:
    print("no. is divisible by 3 and last digit is 4")
else:
    print("either no. is not divisible by 3 or the last digit is not 4")