a=list(input())

while(len(a)>1):
    b=int(input())
    if b>=len(a):
        a.pop()
    else:
        a.pop(b)

    for i in a:
        print(i,end="")
    print()