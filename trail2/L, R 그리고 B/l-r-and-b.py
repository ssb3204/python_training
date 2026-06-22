board = [list(input()) for _ in range(10)]

in_one_line=False
# Please write your code here.
for i in range(10):
    for j in range(10):
        if board[i][j]=="B":
            B_idx=(i,j)
        elif board[i][j]=="L":
            L_idx=(i,j)
        elif board[i][j]=="R":
            R_idx=(i,j)

if B_idx[0]==L_idx[0] and L_idx[0]==R_idx[0]:
    if L_idx[1]<R_idx[1]<B_idx[1]:
        in_one_line=True
    elif L_idx[1]>R_idx[1]>B_idx[1]:
        in_one_line=True
elif B_idx[1]==L_idx[1] and L_idx[1]==R_idx[1]:
    if L_idx[0]<R_idx[0]<B_idx[0]:
        in_one_line=True
    elif L_idx[0]>R_idx[0]>B_idx[0]:
        in_one_line=True




if in_one_line:
    print(abs(L_idx[0]-B_idx[0])+abs(L_idx[1]-B_idx[1])+1)

else:
    print(abs(L_idx[0]-B_idx[0])+abs(L_idx[1]-B_idx[1])-1)
