t=0
f=0
for _ in range(10):
    a=int(input())
    if a%3==0 and a%5==0:
        t+=1
        f+=1
    elif a%3==0:
        t+=1
    elif a%5==0:
        f+=1
    
print(t,f,sep=" ")