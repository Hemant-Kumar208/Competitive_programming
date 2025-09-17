arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(arr)
num = int(input("select the number whose index you want to know: "))
for i in range (len(arr)):
    if(num==arr[i]):
        print("Index: ", i)
        
