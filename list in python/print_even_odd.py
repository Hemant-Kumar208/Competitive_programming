arr = list(map(int,input("Enter numbers: ").split()))

print("odd numbers in array: ")
for i in arr:
    if i%2!=0:
        print(i)
print()
print("Even numbers in array: ")
for j in arr:
    if j%2==0:
        print(j)

    