n = int(input())
a = list(map(int, input().split()))

total=0
# Please write your code here.
for i in range(100):
    cnt=0
    for j in range(len(a)):
        for k in range(j+1,len(a)):
            if a[j]-i ==i-a[k]:

                cnt+=1
    if total<cnt:
        total=cnt

print(total)