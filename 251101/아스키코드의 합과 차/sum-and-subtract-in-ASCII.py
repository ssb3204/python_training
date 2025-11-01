a,b=input().split()


if ord(b)>ord(a):
    num=ord(b)-ord(a)
else:
    num=ord(a)-ord(b)
print(ord(a)+ord(b),num,sep=" ")