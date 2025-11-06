N = int(input())

# Please write your code here.
def f(a):
    if a==1:
        return 1
    return f(a-1)+a

print(f(N))

