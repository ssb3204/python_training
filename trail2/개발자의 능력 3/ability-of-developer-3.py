abilities = list(map(int, input().split()))

min_num=1000000
# Please write your code here.
for i in range(4):
    for j in range(4):
        for k in range(4):
            left_over=abilities.copy()
            ext=[left_over.pop(i),left_over.pop(j),left_over.pop(k)]
            diff=abs(sum(ext)-sum(left_over))

            if diff<min_num:
                min_num=diff
            

print(min_num)

