A, B, C = map(int, input().split())

# Please write your code here.
n=C//A
m=C//B

mn=0
for i in range(n+1):
    for j in range(m+1):
        total=0
        total=A*i+B*j

        if total<=C and mn <total:
            mn=total
    

print(mn)