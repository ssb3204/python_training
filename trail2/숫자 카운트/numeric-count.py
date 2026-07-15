n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)
num1=0
all_pass=True
total=0
# Please write your code here.
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or i==k or j==k:
                continue
            num=[i,j,k]
            all_pass=True
            for x in range(n):
                num1=a[x]
                h=num1//100
                t=(num1//10)%10
                o=num1%10
                num2=[h,t,o]
                c1=b[x]
                c2=c[x]

                cnt_one=0
                cnt_two=0
                for y in range(3):
                    if num[y]==num2[y]:
                        cnt_one+=1
                    elif num[y] in num2:
                        cnt_two+=1
                    
                if cnt_one!=c1 or cnt_two!=c2:
                    all_pass=False
                    break

            if all_pass:
                total+=1
print(total)