a=int(input())

for i in range(1,2*a+2):
    for j in range(1,2*a+2):
        if j%2==0 and i%2==0:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
