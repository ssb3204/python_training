N = int(input())

# Please write your code here.
def f(a):
    if a%2==0:
        if a==2:
            return 2
        else:
            return f(a-2)+a
    else:
        if a==1:
            return 1
        else:
            return f(a-2)+a
    
print(f(N))
        
    
