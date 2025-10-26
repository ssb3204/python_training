a=int(input())

for i in range(a):
    for j in range(a-i,a+1):
        print(j,end=" ")
    print()
