a=int(input())

ls=[[0]*a for _ in range(a)]
cnt=1
for i in range(a):
        if i%2==0:
            for j in range(a):
                ls[i][j]=cnt
                cnt+=1
        else:
            for j in range(a-1,-1,-1):
                ls[i][j]=cnt
                cnt+=1

for i in ls:
    print(" ".join(map(str,i)))