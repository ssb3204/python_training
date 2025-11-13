n = int(input())

# Please write your code here.
ls=[]
while True:
    if n<2:
        ls.append(n)
        break
    ls.append(n%2)
    n=n//2


for i in ls[::-1]:
    print(i,end="")