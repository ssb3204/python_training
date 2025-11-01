a=input()
b=input()
cnt=0
while(True):
    if a==b:
        print(cnt)
        break
    if cnt>len(a):
        print("-1")
        break
    a=a[-1:]+a[:-1]
    cnt+=1