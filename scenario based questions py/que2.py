n = list(map(int, input("Enter marks: ").split()))
count=0
for i in n:
    if i%2==0:
        print(i,end=" ")
        count+=1
if count==0:
    print("-1")