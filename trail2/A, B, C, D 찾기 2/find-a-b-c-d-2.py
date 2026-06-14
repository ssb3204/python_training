nums = list(map(int, input().split()))
nums.sort()
# Please write your code here.
for i in range(1,41):
    for j in range(i,41):
        for k in range(j,41):
            for x in range(k,41):
                ls=[i,j,k,x,i+j,j+k,k+x,x+i,i+k,j+x,i+j+k,i+j+x,i+k+x,j+k+x,i+j+k+x]
                ls.sort()
                if ls==nums:
                    print(i,j,k,x,sep=" ")

                