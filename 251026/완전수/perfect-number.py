start, end = map(int, input().split())

# Please write your code here.
cnt=0
sum=0
for i in range(start,end+1):
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        cnt+=1
print(cnt)
        