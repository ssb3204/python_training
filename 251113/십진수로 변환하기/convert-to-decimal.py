ls = list(input())

# Please write your code here.
sum=0
n=0
for i in reversed(ls):
    if i=="1":
        sum+=(2**n)
    n+=1

print(sum)