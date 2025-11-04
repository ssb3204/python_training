a, b = map(int, input().split())

# Please write your code here.
def f(a,b):
    if a>b:
        a+=25
        b*=2
        return a,b
    else:
        b+=25;a*=2
        return a,b

a,b=f(a,b)
print(a,b)