a=int(input())

c=0
w=0
t=0

for i in range(1,a+1):
    if i%12==0:
        t+=1
    elif i%3==0:
        w+=1
    elif i%2==0:
        c+=1

print(c,w,t,sep=" ")