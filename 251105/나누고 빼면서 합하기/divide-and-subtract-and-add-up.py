n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def f(a):
    global m
    if a%2==0:
        m//=2
    else:
        m-=1

sum=0
while(True):
    sum+=A[m-1]
    f(m)
    if m<1:
        break
print(sum)