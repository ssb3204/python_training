n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class std:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    
ls=[]

for i in range(n):
    ls.append(std(name[i],score1[i],score2[i],score3[i]))

ls.sort(key=lambda x: x.b+x.c+x.d)

for i in ls:
    print(i.a,i.b,i.c,i.d,sep=" ")