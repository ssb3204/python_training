N = int(input())
seats = input()

# Please write your code here.
total=0

for i in range(N):
    ls=list(seats)

    if ls[i]!='1':
        ls[i]='1'

        now=0
        min_dis=1001
        for j in range(1,N):

            if ls[j]=='1':
                dis=j-now
                if min_dis>dis:
                    min_dis=dis
                now=j                
        if total<min_dis:
            total=min_dis

print(total)