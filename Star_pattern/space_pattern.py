n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
for i in range (0,n):
    for j in range(0,m):
         if j==1 or j==3:
              print("*",end=" ")
         else:
              print(" ",end=" ")
    print()
    