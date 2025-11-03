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
    elif a in [2,4,6,9,11]:
        if b<=30:
            return True
        else:
            return False
    else:
        return False

print("Yes" if f(M,D) else "No")
