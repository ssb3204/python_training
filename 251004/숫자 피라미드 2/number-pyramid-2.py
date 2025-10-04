a=int(input())
num=1
for i in range(1,a+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
