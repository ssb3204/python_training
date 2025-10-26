a=int(input())
cnt=0
for i in range(65,65+(a**2)):
    print(chr(i),end="")
    cnt+=1
    if cnt%a==0:
        print()