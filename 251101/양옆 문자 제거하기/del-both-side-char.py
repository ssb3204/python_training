a=list(input())


a.remove(a[1])
a.remove(a[-2])

for i in a:
    print(i,end="")