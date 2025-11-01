a=input()
    
b=list(input().split())
b="".join(b)

for i in range(0,len(b)):
    if i!=0 and i%5==0:
        print()
    print(b[i],end="")