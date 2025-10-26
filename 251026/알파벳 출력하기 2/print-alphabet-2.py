a=int(input())
num=65
for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(a,0,-1):
        if num==91:
            num=65
        print(chr(num),end=" ")
        num+=1
    print()