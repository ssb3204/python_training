a=list(input())


del a[1]
del a[len(a)-2]

for i in a:
    print(i,end="")