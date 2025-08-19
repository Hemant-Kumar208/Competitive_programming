A = int(input("Enter A: "))
rev = 0
temp = A
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
if rev == A:
    print("Yes")
else:
    print("No")

