n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class std:
    def __init__(self,n,h,w):
        self.n=n
        self.h=h
        self.w=w

ls=[]

for i in range(5):
    ls.append(std(name[i],height[i],weight[i]))

ls.sort(key=lambda x:x.n)
print("name")
for i in ls:
    print(i.n,i.h,i.w,sep=" ")
print()
ls.sort(key=lambda x:-x.h)
print("height")
for i in ls:
    print(i.n,i.h,i.w,sep=" ")