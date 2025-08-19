N = int(input("Enter A: "))
s = 0
i = 1
while i <= N:
    if i % 2 != 0:
        s = s + i
    i = i + 1
print("Sum of odd =", s)
