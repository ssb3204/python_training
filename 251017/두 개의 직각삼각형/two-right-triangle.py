a=int(input())

for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    for j in range((a-i)*2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()