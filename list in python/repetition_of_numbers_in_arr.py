arr = list(map(int, input("Enter numbers: ").split()))

for i in arr: 
    count = arr.count(i)
    if count > 1:
        print(i, "is repeated", count, "times")
