num = int(input("Enter a number : "))
a = num%5
b = num%11
if a == 0 and b==0:
    print("no. is divisible by 5 and 11 both")
else:
    print("either no. is not divisible by 5 or 11")