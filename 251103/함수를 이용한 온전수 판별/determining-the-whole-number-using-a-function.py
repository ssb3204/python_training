a, b = map(int, input().split())

# Please write your code here.
def f(a):
    if a%2==0:
        return False
    if a%10==5:
        return False
    if a%3==0 and a%9!=0:
        return False
    return True

cnt=0
for i in range(a,b+1):
    if f(i):
        cnt+=1

print(cnt)