N = int(input())
seats = input()

# Please write your code here.
total=0

for i in range(N):
    ls=list(seats)

    if ls[i]!='1':
        ls[i]='1'


        min_gap = 1001
        for j in range(N):
            if ls[j]=='1':
                now=j
                dis=1001
                for k in range(j+1,N):
                    if ls[k]=='1':
                        now2=k
                        dis=now2-now
                        break
            min_gap=min(min_gap,dis)
    
        if total<min_gap:
            total=min_gap

print(total)
