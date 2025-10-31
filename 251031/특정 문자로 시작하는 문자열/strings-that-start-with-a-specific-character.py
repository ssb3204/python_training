a=int(input())
ls=[]
sum=0
cnt=0

for _ in range(a):
    b=input()
    ls.append(b)

c=input()

for i in ls:
    if i.startswith(c):
        sum+=len(i)
        cnt+=1

print(f"{cnt} {sum/cnt:.2f}")