X, Y = map(int, input().split())


mx=0
# Please write your code here.
for i in range(X,Y+1):
    total=0
    while(i>0):
        total+=i%10
        i//=10
    mx=max(total,mx)
print(mx)