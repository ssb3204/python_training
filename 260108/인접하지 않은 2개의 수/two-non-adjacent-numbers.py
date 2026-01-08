n = int(input())
numbers = list(map(int, input().split()))
max=0
# Please write your code here.
for i in range(n):
    sum=0
    if i==0:
        for j in range(i+1,n):
            sum=numbers[i]+numbers[j]
            if max<sum:
                max=sum
    elif i==(n-1):
        for j in range(n-2):
            sum=numbers[i]+numbers[j]
            if max<sum:
                max=sum
    else:
        for j in range(n):
            if j==i-1 or j==i+1 or j==i:
                continue
            else:
                sum=numbers[i]+numbers[j]
            if max<sum:
                max=sum
print(max)

