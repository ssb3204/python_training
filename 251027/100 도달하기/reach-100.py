a=int(input())

f=1
s=a
print(f,a,sep=' ',end=' ')
while(True):
    num=f+s
    print(num,end=' ')
    f=s
    s=num
    if s>100:
        break