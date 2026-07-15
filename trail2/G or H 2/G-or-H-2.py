n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

arr=sorted(people, key=lambda x:int(x[0]))
total=0
for i in range(n):
    l=0
    for j in range(n,-1,-1):
        ls=[]
        
        start=-1
        end=-1

        for k in range(i,j):
            if k==i:
                start=int(arr[k][0])
            if k==j-1:
                end=int(arr[k][0])
            ls.append(arr[k][1])
            
        g_cnt=0
        h_cnt=0
        if len(ls)==0:
            break
        for k in range(len(ls)):
            if ls[k]=='G':
                g_cnt+=1
            else:
                h_cnt+=1
    
        
        if g_cnt==0 and h_cnt!=0:
            if total<end-start:
                total=end-start
        elif g_cnt!=0 and h_cnt==0:
            if total<end-start:
                total=end-start
        elif (g_cnt!=0 and h_cnt!=0) and g_cnt==h_cnt:
            if total<end-start:
                total=end-start

print(total)