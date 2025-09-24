n = list(map(int, input("Enter marks: ").split()))
count = 0
count_pass = 0
for i in n:
    if i<35:
        count+=1
for i in n:
    if i>=35:
        count_pass+=1
print(count_pass,count)
        
    
    
