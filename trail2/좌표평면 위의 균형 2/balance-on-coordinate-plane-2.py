n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_list=[]

for i in range(0,102,2):
    for j in range(0,102,2):
        pp=0
        pm=0
        mm=0
        mp=0
        for a,b in points:
            if i<a and j<b:
                pp+=1
            elif i<a and j>b:
                pm+=1
            elif i>a and j>b:
                mm+=1
            else:
                mp+=1
        max_list.append(max(pp,pm,mm,mp))

print(min(max_list))