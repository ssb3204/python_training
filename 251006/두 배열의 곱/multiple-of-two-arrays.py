lf = [list(map(int,input().split())) for _ in range(3)]
input()
ls = [list(map(int,input().split())) for _ in range(3)]




for i in range(3):
    for j in range(3):
        print(lf[i][j]*ls[i][j],end=" ")
    print()