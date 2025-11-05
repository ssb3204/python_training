n = int(input())

# Please write your code here.
def f(a):
    if a==0:
        return
    f(a-1)
    print(a,end=" ")

def g(a):
    if a==0:
        return
    print(a,end=" ")
    g(a-1)

f(n)
print()
g(n)