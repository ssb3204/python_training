N = int(input())

# Please write your code here.
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    
    return fib(n-1)+fib(n-2)

num=fib(N)
print(num)
