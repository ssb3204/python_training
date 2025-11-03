n = int(input())

# Please write your code here.
def f(a):
    sum=0
    for i in range(1,a+1):
        sum+=i
    print(sum//10)

f(n)