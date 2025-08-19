A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = 1
i = 1
while i <= B:
    result = result * A
    i = i + 1
print(A,"^",B,"=",result)