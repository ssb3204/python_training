ls =list(map(str,input().split()))
num=[]
for i in ls:
    for j in i:
        if not j.isdigit():
            a,b=i.split(j)
            num.append(a)
    
sum=0
for i in num:
    sum+=int(i)

print(sum)




