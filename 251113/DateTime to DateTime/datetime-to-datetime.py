a, b, c = map(int, input().split())

# Please write your code here.

if a==11 and b<11:
    print(-1)
elif a==11 and b==11 and c<11:
    print(-1)
else:
    sum=0
    sum+=(a-11)*24*60
    sum+=(b-11)*60
    sum+=(c-11)
    print(sum)
