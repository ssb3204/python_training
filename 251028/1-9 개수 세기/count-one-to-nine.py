a=int(input())

ls=[0]*9
b=list(map(int,input().split()))
for i in range(a):
    ls[b[i]-1]+=1

for i in ls:
    print(i)