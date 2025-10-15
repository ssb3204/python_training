a,b=map(int,input().split())

i=1
while i!=a:
    if i%b==0:
        print("1")
    else:
        print("0")
    i+=1