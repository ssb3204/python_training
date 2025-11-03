a, b, c = map(int, input().split())

# Please write your code here.

def f(i,j,k):
    if i<=j and i<=k:
        print(i)
    elif j<=i and j<=k:
        print(j)
    elif k<=i and k<=j:
        print(k)


f(a,b,c)