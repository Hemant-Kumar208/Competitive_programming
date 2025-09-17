arr = list(map(int,input("Enter numbers: ").split()))
sum_odd = 0
sum_even = 0
for i in arr:
    if i%2!=0:
        sum_odd += i
for i in arr:
    if i%2==0:
        sum_even += i
print(sum_even)
print(sum_odd)
diff = sum_even - sum_odd
print("Diffrence between odd and even numbers: ", diff)
    