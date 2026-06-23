n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

last=[]
cnt=0
where=[0,0,0]
pre=["A","B","C"]


def check_head():
    num=max(where)
    if where[0]==num:
        last.append("A")
    if where[1]==num:
        last.append("B")
    if where[2]==num:
        last.append("C")
    
    return last
# Please write your code here.
for i in range(n):
    last=[]
    if c[i]=="A":
        where[0]+=s[i]
        check_head()
        if last!=pre:
            cnt+=1
    elif c[i]=="B":
        where[1]+=s[i]
        check_head()
        if last!=pre:
            cnt+=1
    elif c[i]=="C":
        where[2]+=s[i]
        check_head()
        if last!=pre:
            cnt+=1
    pre=last.copy()

print(cnt)