N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0]=='size':
        print(len(value))
    elif line[0]=='empty':
        if len(value)==0:
            print(1)
        else:
            print(0)
    elif line[0]=='pop':
        print(value[-1])
        del value[-1]
    elif line[0]=='top':
        print(value[-1])
