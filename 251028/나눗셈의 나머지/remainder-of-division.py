a,b=map(int,input().split())
ls=[0]*b
while(True):
    if a<=1:
        break
    a=a//b
    ls[a%b]+=1

sum=0
for i in ls:
    sum+=i**2
print(sum)