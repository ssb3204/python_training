n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class std:
    def __init__(self,x,y,n):
        self.n=n
        self.x=x
        self.y=y

ls=[]

for i in range(n):
    ls.append(std(students[i][0], students[i][1], students[i][2]))

ls.sort(key=lambda x:(x.x, -x.y))

for i in ls:
    print(i.x,i.y,i.n,sep=" ")