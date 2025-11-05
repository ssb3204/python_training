n = int(input())

# Please write your code here.
def f(a):
    if a==0:
        return
    f(a-1)
    print("*"*a,end="")
    print()

f(n)