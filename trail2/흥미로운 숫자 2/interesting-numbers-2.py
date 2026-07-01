X, Y = map(int, input().split())
cnt=0
# Please write your code here.
for i in range(X,Y+1):
    num_string=str(i)
    ls={}
    for j in range(len(num_string)):
        if num_string[j] not in ls:
            ls[num_string[j]]=1
        else:
            ls[num_string[j]]+=1
    
    if len(ls)==2:
        if 1 in ls.values():
            cnt+=1

print(cnt)