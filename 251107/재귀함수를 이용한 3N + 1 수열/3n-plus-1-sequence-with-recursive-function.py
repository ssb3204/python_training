n = int(input())
# Please write your code here.
def f(a):
    if a%2==0:
        if a==1:
            return 0 
        return f(a//2)+1
    else:
        if a==1:
            return 0 
        return f(a*3+1)+1
    
print(f(n))