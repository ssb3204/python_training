a=int(input())
c=0
for i in range(a):
    b=list(map(int,input().split()))
    sum=0
    cnt=0
    for j in b:
        cnt+=1
        sum+=j
    if sum/cnt>=60:
        print("pass")
        c+=1
    else:
        print("fail")

print(c)