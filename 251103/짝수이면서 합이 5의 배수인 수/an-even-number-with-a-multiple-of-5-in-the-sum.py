n = int(input())

# Please write your code here.
def f(a):
    if a%2==0:
        if ((a%10)+(a//10))%5==0:
            return 1
if f(n):
    print("Yes")
else:
    print("No") 