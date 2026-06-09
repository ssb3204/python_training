X, Y = map(int, input().split())
cnt=0
# Please write your code here.
for i in range(X,Y+1):
    s= str(i)

    if str(i)==s[::-1]:
        cnt+=1

print(cnt)