lf = list(map(int,input().split()))
ls = list(map(int,input().split()))
ld = list(map(int,input().split()))

lf = [i*3 for i in lf]
ls = [i*3 for i in ls]
ld = [i*3 for i in ld]

for i in lf:
    print(i,end=" ")
print()
for i in ls:
    print(i,end=" ")
print()
for i in ld:
    print(i,end=" ")