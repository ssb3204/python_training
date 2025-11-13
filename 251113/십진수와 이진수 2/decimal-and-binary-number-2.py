ls = list(input())

# Please write your code here.
sum=0
n=0
for i in ls[::-1]:
    if i=="1":
        sum+=2**n
    n+=1

sum*=17

print(bin(sum)[2:])