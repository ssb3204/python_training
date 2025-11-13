ls = list(input())

# Please write your code here.
sum=0
n=0
for i in ls[::-1]:
    if i=="1":
        sum+=2**n
    n+=1

sum*=17

num=[]

while True:
    if sum<2:
        num.append(sum)
        break
    num.append(sum%2)
    sum//=2

for i in num[::-1]:
    print(i,end="")