n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
total=0

num=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a=arr[i]
            b=arr[j]
            c=arr[k]
            
            carry=False


            for x in range(1,5):
                cnt=0
                if len(str(a))>=x:
                    cnt+=int(str(a)[-x])
                if len(str(b))>=x:
                    cnt+=int(str(b)[-x])
                if len(str(c))>=x:
                    cnt+=int(str(c)[-x])
                
                if cnt>=10:
                    carry=True
                    break

            if carry==False:
                num=a+b+c

        if total<num:
            total=num      

if total!=0:
    print(total)
else:
    print(-1)