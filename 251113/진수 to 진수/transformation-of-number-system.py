a, b = map(int, input().split())
n = list(input())

# Please write your code here.

sum=0
n=0
for i in n[::-1]:
    if i=="1":
        sum+=a**n
    n+=1

num=[]
while True:
    if sum<a:
        num.append(sum)
        break
    num.append(num%b)
    sum//=b

for i in num[::-1]:
    print(i,end="")