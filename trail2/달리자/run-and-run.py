n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
total=0
num=0
for i in range(n-1):
    if i==0:
        num=A[i]-B[i]
        total+=num
    else:
        num+=A[i]-B[i]
        total+=num
    
print(total)