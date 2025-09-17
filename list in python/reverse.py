arr=list(map(int,input("Enter numbers separated by space: ").split()))
reversed_list = []
for i in arr:
    reversed_list.insert(0, i)
print("Original List:", arr)
print("Reversed List:", reversed_list)
