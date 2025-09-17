arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(arr)
print("negative numbers in array : ")
for i in arr:
    if i<0:
        print(i)