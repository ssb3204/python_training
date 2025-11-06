N = int(input())

# Please write your code here.
def f(a):
    if a<10:
        return a**2
    return f(a//10)+(a%10)**2

print(f(N))