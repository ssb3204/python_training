a, b = map(int, input().split())

# Please write your code here.

def f(a):
    is_t=True
    for i in range(2,a):
        if a%i==0:
            is_t=False
    return is_t
sum=0
for i in range(a,b+1):
    if f(i):
        sum+=i
print(sum)