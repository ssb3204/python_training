cnt=0
ls=[]
while(True):
    a=input()
    ls.append(a)
    if a=="0":
        break
    else:
        cnt+=1
    

print(cnt)
for i in range(0,len(ls),2):
    print(ls[i])