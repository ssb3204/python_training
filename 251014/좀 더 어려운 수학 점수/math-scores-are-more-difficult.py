a,b=map(int,input().split())
x,y=map(int,input().split())

if x>a:
    print("B")
elif a>x:
    print("A")
else:
    if b>y:
        print("A")
    elif y>b:
        print("B")
