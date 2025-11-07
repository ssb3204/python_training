a, b, c = map(int, input().split())

# Please write your code here.
def f(a):
    if a<10:
        return a
    return f(a//10)+a%10

num=a*b*c
print(f(num))