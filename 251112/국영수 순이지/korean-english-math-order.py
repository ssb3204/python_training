n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class std:
    def __init__(self,name,k,e,m):
        self.name=name
        self.k=k
        self.e=e
        self.m=m

ls=[]

for i in range(n):
    ls.append(std(name[i],korean[i],english[i],math[i]))

ls.sort(key=lambda x: (x.k, x.e, x.m))

for i in ls[::-1]:
    print(i.name,i.k,i.e,i.m,sep=" ")