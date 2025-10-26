a=int(input())
num=65
for i in range(1,a+1):
    for j in range(i):
        if num==91:
            num=65
        print(chr(num),end="")
        num+=1
    print()
    
