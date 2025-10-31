a=input()
ls=[]
for i in range(len(a)):
    if (i+1)%2==0:
        ls.append(a[i])
ls.reverse()

for i in ls:
    print(i,end="")