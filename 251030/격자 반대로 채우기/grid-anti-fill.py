a=int(input())

ls=[[0 for _ in range(a)] for _ in range(a)]
cnt=1
for i in range(a-1,-1,-1):
    for j in range(a-1,-1,-1):
        if a%2!=0:
            if i%2==0:
                ls[j][i]=cnt
                cnt+=1
            else:
                ls[a-1-j][i]=cnt
                cnt+=1
        else:
            if i%2!=0:
                ls[j][i]=cnt
                cnt+=1
            else:
                ls[a-1-j][i]=cnt
                cnt+=1

for i in ls:
    for j in i:
        print(j,end=" ")
    print()