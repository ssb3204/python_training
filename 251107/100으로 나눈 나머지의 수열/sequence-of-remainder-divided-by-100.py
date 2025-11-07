N = int(input())

# Please write your code here.
def f(a):
    if a==1:
        return 2
    if a==2:
        return 4
    return (f(a-1)*f(a-2))%100

print(f(N))