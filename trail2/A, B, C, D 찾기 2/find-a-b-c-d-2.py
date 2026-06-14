nums = list(map(int, input().split()))
nums.sort()
# Please write your code here.
for i in range(1,41):
    for j in range(i,41):
        for k in range(j,41):
            for x in range(k,41):
                ls=[]
                ls.append(i)
                ls.append(j)
                ls.append(k)
                ls.append(x)
                ls.append(i+j)
                ls.append(j+k)
                ls.append(k+x)
                ls.append(x+i)
                ls.append(i+k)
                ls.append(j+x)
                ls.append(i+j+k)
                ls.append(i+j+x)
                ls.append(i+k+x)
                ls.append(j+k+x)
                ls.append(i+j+k+x)
                ls.sort()
                if ls==nums:
                    print(i,j,k,x,sep=" ")

                