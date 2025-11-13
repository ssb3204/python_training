N, B = map(int, input().split())

# Please write your code here.
ls=[]
while True:
    if N<B:
        ls.append(N)
        break
    ls.append(N%B)
    N=N//B

for i in ls[::-1]:
    print(i,end="")