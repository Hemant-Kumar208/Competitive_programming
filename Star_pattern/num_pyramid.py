n = int(input("Enter a number: "))
for i in range (n):
    for j in range (i+2):
        if j > 0:
            print(j,end=" ")
        else:
            print("",end="")
    print()