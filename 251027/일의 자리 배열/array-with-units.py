a,b=map(int,input().split())

f=a
s=b
print(f,s,sep=" ",end=" ")
for _ in range(8):
    num=f+s
    print(num%10,end=" ")
    f=b
    s=num

