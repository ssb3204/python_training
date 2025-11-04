a, b = map(int, input().split())

# Please write your code here.

def f(a,b):
    if a>b:
        b+=10
        a*=2
        return b,a
    else:
        a+=10
        b*=2
        return a,b
    


a,b=f(a,b)
print(a,b,sep=" ")