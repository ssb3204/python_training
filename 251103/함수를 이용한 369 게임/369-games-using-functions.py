a, b = map(int, input().split())

# Please write your code here.
def three(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0:
            cnt+=1
        else:
            if tes(i):
                cnt+=1
    return cnt

def tes(a):
    cnt=0
    if "3" in str(a) or "6" in str(a) or "9" in str(a):
        return 1
    
print(three(a,b))