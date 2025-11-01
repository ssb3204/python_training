a=list(input())

for i in range(len(a)-1):
    if a[i]=='e':
        a.pop(i)
        break


for i in a:
    print(i,end="")