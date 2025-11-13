a, b = map(int, input().split())
ls = list(input())

# Please write your code here.

sum=0
n=0
for i in ls[::-1]:
    if i!="0":
        sum+=int(i)*(a**n)
    n+=1

num=[]
while True:
    if sum<b:
        num.append(sum)
        break
    num.append(sum%b)
    sum//=b

for i in num[::-1]:
    print(i,end="")