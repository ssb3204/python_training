a=int(input())

for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()
