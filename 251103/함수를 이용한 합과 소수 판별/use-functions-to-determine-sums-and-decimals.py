a, b = map(int, input().split())

# Please write your code here.
def f(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
        
def even(i):
    if ((i%10)+(i//10))%2==0:
        return True

cnt=0
for i in range(a,b+1):
    if f(i) and even(i):
        cnt+=1

print(cnt)