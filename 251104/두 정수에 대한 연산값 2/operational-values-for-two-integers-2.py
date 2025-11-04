a, b = map(int, input().split())

# Please write your code here.

def f(a,b):
    mi=min(a,b)+10
    ma=max(a,b)*2
    print(mi,ma,sep=" ")


f(a,b)
