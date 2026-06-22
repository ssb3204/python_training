n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.
ls=a.copy()
ls.sort()
now_first=True
num=ls[1]
cnt=0

for i in range(1,len(a)):
    if ls[i]>num:
        now_first=False
        second=ls[i]
        break

if now_first:
    print("-1")
else:
    for i in range(1,len(a)):
        if a[i]==second:

            cnt+=1
            second_idx=i
    
    if cnt!=1:
        print("-1")
    else:
        print(second_idx)
