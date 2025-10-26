a=int(input())

for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    