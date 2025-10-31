a=input()

e=0
b=0

for i in range(len(a)-1):
    if a[i:i+2]=='ee':
        e+=1
    elif a[i:i+2]=='eb':
        b+=1

print(e,b,sep=" ")