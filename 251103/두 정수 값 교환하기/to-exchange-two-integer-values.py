n, m = map(int, input().split())
# Please write your code here.
def f(a,b):
    a,b=b,a
    return a,b
    
n,m=f(n,m)
print(n,m)