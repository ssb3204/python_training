arr = list(map(int, input().split()))

arr.sort()
# Please write your code here.
A=arr[0]
B=arr[1]
C=0
for i in range(B,A+B+1):
    if i in arr and i+A+B in arr:
        C=i
        break

D=max(arr)-A-B-C
print(A,B,C,D)