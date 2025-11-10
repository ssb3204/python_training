n = int(input())
arr = list(map(int, input().split()))
ls=[]
num=0
# Please write your code here.
for i in range(n):
    ls.append(arr[i])
    if i%2==0:
        ls.sort()
        print(ls[num],end=" ")
        num+=1
