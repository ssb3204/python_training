n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.

class std:
    def __init__(self,h,w,n):
        self.h=h
        self.w=w
        self.n=n

ls=[]
for i in students:
    ls.append(std(i[0],i[1],i[2]))

ls.sort(key=lambda x:(-x.h ,-x.w, x.n))

for i in ls:
    print(i.h,i.w,i.n,sep=" ")


