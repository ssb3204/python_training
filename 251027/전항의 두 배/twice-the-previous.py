a,b=map(int,input().split())

f=a
s=b
print(f,s,sep=" ",end=" ")
for _ in range(8):
    num=f*2+s
    print(num,end=" ")
    f=s
    s=num
