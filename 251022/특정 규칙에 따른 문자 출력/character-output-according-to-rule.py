a=int(input())

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(i):
        print("@",end=" ")
    print()

for i in range(a-1,0,-1):
    for j in range(i):
        print("@",end=" ")
    for i in range(a-i):
        print(" ",end=" ")
    
    print()
    