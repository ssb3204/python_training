ls =list(map(str,input().split()))
num=[]
is_t=False
for i in ls:
    for j in i:
        if not j.isdigit():
            is_t=True
            a,b=i.split(j)
            num.append(a)
            break
    if is_t==False:
        num.append(j)
        
    
sum=0
for i in num:
    sum+=int(i)

print(sum)




