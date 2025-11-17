n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ls=[0]
sum=1
num=0
for i in range(n-2):
    if arr[i]==arr[i+1]:
        num+=1
    else:
        ls.append(num)
        num=0
ls.sort(reverse=True)
print(sum+ls[0])
        