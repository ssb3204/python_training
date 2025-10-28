a,b=map(int,input().split())

ls= list(map(int,input().split()))

try:
    for _ in range(a):
        q=list(map(int,input().split()))
    
        if q[0]==1:
            print(ls[q[1]-1])
        elif q[0]==2:
            if q[1] not in ls:
                print("0")
            else:
                print(ls.index(q[1])+1)
        elif q[0]==3:
            for i in range(q[1]-1,q[2]):
                print(ls[i],end=" ")
            print()
except EOFError:
    pass