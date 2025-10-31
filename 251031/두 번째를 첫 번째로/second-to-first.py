a=list(input())
f=a[0]
s=a[1]
for i in range(len(a)):
    if a[i]==s:
        a[i]=f

for i in a:
    print(i,end="")