a=int(input())

for i in range(1,a+1):
    for j in range(1,a+1):
        if i==1 or (j%2==0 and j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()       