N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] =="push_front" :
        A.insert(0,int(line[1]))
    elif line[0]=="push_back":
        A.insert(len(A),int(line[1]))
    elif line[0]=="pop_front":
        print(A.pop(0))
    elif line[0]=="pop_back":
        print(A.pop(-1))
    elif line[0]=="size":
        print(len(A))
    elif line[0]=="empty":
        if len(A)==0:
            print("1")
        else:
            print("0")
    elif line[0]=="front":
        print(A[0])
    elif line[0]=="back":
        print(A[-1])
# Please write your code here.