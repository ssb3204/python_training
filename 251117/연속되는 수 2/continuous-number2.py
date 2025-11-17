n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ls=[]
sum=1
num=0
for i in range(n-1):
    if arr[i]==arr[i+1]:
        num+=1
    else:
        ls.append(num)
        num=0
ls.append(num)

if len(ls)==0:
    print(sum)
else:
    ls.sort(reverse=True)
    print(sum+ls[0])
        