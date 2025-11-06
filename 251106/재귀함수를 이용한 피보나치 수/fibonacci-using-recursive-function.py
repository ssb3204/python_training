N = int(input())

# Please write your code here.
def f(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    return f(a-2)+f(a-1)

print(f(N))
    