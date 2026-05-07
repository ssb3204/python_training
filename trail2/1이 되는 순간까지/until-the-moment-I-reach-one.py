N = int(input())
   
# Please write your code here.
def fact(n):
    if n==1:
        return 0

    if n%2==0:
        return fact(n//2)+1
    else:
        return fact(n//3)+1

num=fact(N)
print(num)