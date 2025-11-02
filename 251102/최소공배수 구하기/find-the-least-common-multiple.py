n, m = map(int, input().split())

# Please write your code here.
def lcm(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i

print(lcm(n,m))