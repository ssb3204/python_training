N = int(input())
# Please write your code here.
def f(a):
    if a==1:
        return 1
    if a%2==0:
        return f(a//2)+1
    elif a%2!=0:
        return f(a//3)+1


print(f(N)-1)