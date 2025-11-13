a, b, c = map(int, input().split())

# Please write your code here.

if a<11 or b<11 or c<11:
    print(-1)
sum=0
sum+=(a-11)*24*60
sum+=(b-11)*60
sum+=(c-11)

print(sum)
