start, end = map(int, input().split())

the=0
# Please write your code here.
for i in range(start,end+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==3:
        the+=1
print(the)


