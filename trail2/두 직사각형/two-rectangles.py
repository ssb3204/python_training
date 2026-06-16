x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())


first_sq=[]
sec_sq=[]
end=False
# Please write your code here.
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        first_sq.append((i,j))
    
for i in range(a1,a2+1):
    for j in range(b1,b2+1):
        sec_sq.append((i,j))

for i in first_sq:
    for j in sec_sq:
        if i==j:
            end=True
            break
    
if end:
    print("overlapping")
else:
    print("nonoverlapping")