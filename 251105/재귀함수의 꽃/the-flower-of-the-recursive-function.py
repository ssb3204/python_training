N = int(input())

# Please write your code here.
def f(a):
    if a==0:
        return
    print(a,end=" ")
    f(a-1)
    print(a,end=" ")


f(N)