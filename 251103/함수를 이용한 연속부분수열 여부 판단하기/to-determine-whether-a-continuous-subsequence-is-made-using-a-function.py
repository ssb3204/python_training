n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def f(a,b):
    if n1>n2:
        for i in range(len(a)-len(b)):
            if a[i:i+len(b)]==b:
                return True
    elif n2>n1:
        return False
    else:
        if a==b:
            return True
        else:
            return False

print("Yes" if f(a,b) else "No")

    

