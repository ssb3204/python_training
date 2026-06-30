N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
ls=[]
a1_cnt = 0
b1_cnt = 0
c1_cnt = 0
a2_cnt = 0
b2_cnt = 0
c2_cnt = 0

a_both = 0
b_both = 0
c_both = 0

for i in range(1,N+1):
    ls.append(i)


for i in range(len(ls)):
    da1 = min((a1-ls[i])%N, (ls[i]-a1) %N)
    db1 = min((b1-ls[i])%N, (ls[i]-b1) %N)
    dc1 = min((c1-ls[i])%N, (ls[i]-c1) %N)
    da2 = min((a2-ls[i])%N, (ls[i]-a2) %N)
    db2 = min((b2-ls[i])%N, (ls[i]-b2) %N)
    dc2 = min((c2-ls[i])%N, (ls[i]-c2) %N)

    if da1<= 2:
        a1_cnt += 1
    if db1<= 2:
        b1_cnt += 1
    if dc1<= 2:
        c1_cnt += 1
    if da2<= 2:
        a2_cnt += 1
    if db2<=2:
        b2_cnt += 1
    if dc2<= 2:
        c2_cnt += 1

    if da1<=2 and da2<=2:
        a_both += 1
    if db1<=2 and db2<=2:
        b_both += 1
    if dc1<=2 and dc2<=2:
        c_both += 1

print((a1_cnt*b1_cnt*c1_cnt)+(a2_cnt*b2_cnt*c2_cnt)-(a_both*b_both*c_both))
