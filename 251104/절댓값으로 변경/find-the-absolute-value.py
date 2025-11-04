n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(a):
    for i in a:
        if i<0:
            print(i*-1,end=" ")
        else:
            print(i,end=" ")


f(arr)
