n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

where=[0,0]
head='AB'

cnt=0
# Please write your code here.
for i in range(n):
    last=head
    if c[i]=='A':
        where[0]+=s[i]
    else:
        where[1]+=s[i]

    
    if where[0]>where[1]:
        head ='A'
    elif where[0]<where[1]:
        head ='B'
    else:          
        head ='AB'

    if last!=head:
        cnt+=1

print(cnt)