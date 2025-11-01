cnt=0
while(True):
    a=input()
    if a=="END":
        break
    cnt+=1
    if cnt==10:
        break
    a=list(a)
    a.reverse()
    for i in a:
        print(i,end="")
    print()