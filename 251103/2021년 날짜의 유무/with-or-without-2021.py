M, D = map(int, input().split())

# Please write your code here.
def f(a,b):
    if a in [1,3,5,7,8,10,12]:
        if b<=31:
            return True
        else:
            return False
    elif a==2:
        if b<=28:
            return True
        else:
            return False
    else:
        if b<=30:
            return True
        else:
            return False

print("Yes" if f(M,D) else "No")
