arr1 = list(map(int,input("Enter numbers: ").split()))
arr2 = list(map(int,input("Enter numbers: ").split()))
result = []

for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Added Array:", result)
