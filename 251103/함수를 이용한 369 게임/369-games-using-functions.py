a, b = map(int, input().split())

# Please write your code here.
def three(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0:
            cnt+=1
    return cnt

def tes(a,b):
    cnt=0
    for i in range(a,b+1):
        if "3" in str(i):
            cnt+=1
    return cnt

print(three(a,b)+tes(a,b))