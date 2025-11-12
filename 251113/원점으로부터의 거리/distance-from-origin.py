n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class std:
    def __init__(self,n,d):
        self.n=n
        self.d=d

ls=[]

for i in range(n):
    sum=abs(points[i][1][0]-0)+abs(points[i][1][1]-0)
    points[i]=(points[i][0],sum)

for i in range(n):
    ls.append(std(points[i][0],points[i][1]))

ls.sort(key=lambda x:(x.d,x.n))

for i in ls:
    print(i.n+1)


