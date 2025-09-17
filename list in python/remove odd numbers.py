arr = list(map(int,input("Enter numbers: ").split()))
for i in arr:
    if i%2!=0:
        arr.remove(i)
print(arr)
    