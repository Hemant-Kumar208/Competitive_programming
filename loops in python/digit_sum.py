num = int(input("Enter a number: "))
sum = 0

while(num>0):
    digit = num%10
    num = num//10
    sum = sum + digit
print("sum of digit",sum)