a=int(input())

for i in range(10,10+a*2,2):
    for j in range(1,a+1):
        print(i+(j*2-1),end=" ")
    print()