ls =list(map(str,input().split()))
num=[]

for i in ls:
    for j in i:
        is_t=False
        if not j.isdigit():
            is_t=True
            a=""
            b=""
            a,b=i.split(j)
            num.append(a)
            break
    if is_t==False:
        num.append(i)
        
    
sum=0
for i in num:
    sum+=int(i)

print(sum)