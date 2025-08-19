num = int(input("Enter a number: "))
rev_num = 0

while (num>0):
    digit = num%10
    num = num//10
    rev_num = rev_num*10 + digit
print("reverse number: ",rev_num)