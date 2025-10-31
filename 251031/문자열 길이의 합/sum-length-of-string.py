a=int(input())
sum=0
lo=0
for _ in range(a):
    b=input()
    sum+=len(b)
    if b.startswith("a"):
        lo+=1

print(sum,lo,sep=" ")