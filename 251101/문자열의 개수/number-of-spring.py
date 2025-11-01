cnt=0
ls=[]
while(True):
    a=input()
    if a=="0":
        break
    else:
        ls.append(a)
        cnt+=1
    
print(cnt)

if len(ls)!=0:
    for i in range(0,len(ls),2):
        print(ls[i])