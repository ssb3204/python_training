a=int(input())

for i in range(a):
    for j in range(a):
        if j!=0 and i%2!=0:
            print(" ",end=" ")
        elif j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

        