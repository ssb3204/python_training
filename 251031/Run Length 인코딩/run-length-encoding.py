A = input()
ls=[]
# Please write your code here.
i=0
while(i<len(A)):
    c=A[i]
    cnt=1
    j=i+1
    for k in range(i+1,len(A)):
        if A[i]==A[k]:
            cnt+=1
            j+=1
        else:
            break
    ls.append(c)
    ls.append(cnt)
    i=j


a="".join(str(i) for i in ls)
print(len(a),a,sep="\n")

