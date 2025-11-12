n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class std:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
ls=[]
for i in range(n):
    ls.append(std(name[i],height[i],weight[i]))

ls.sort(key=lambda x:x.height)

for i in ls:
    print(i.name,i.height,i.weight,sep=" ")
