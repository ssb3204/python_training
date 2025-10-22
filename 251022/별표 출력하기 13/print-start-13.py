a= int(input())
o=a
e=1
for i in range(1,a+1):
    if i%2!=0:
        for j in range(o):
            print("*",end=" ")
        print()
        o-=1
    else:
        for j in range(e):
            print("*",end=" ")
        print()
        e+=1

for i in range(a,0,-1):
    if i%2!=0:
        for j in range(e):
            print("*",end=" ")
        print()
        e+=1
    else:
        for j in range(o):
            print("*",end=" ")
        print()
        o-=1