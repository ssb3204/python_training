inp = [input() for _ in range(3)]

# Please write your code here.
def check(arr):
    arr=sorted(set(arr))
    if len(arr)==2:
        return tuple(arr)
    else:
        return None 

total=set()
cnt=0
for i in range(3):
    num=check([inp[i][j] for j in range(3)])
    if num:
        total.add(num)
    num=check([inp[j][i] for j in range(3)])
    if num:
        total.add(num)

num=check([inp[0][0],inp[1][1],inp[2][2]])
if num:
    total.add(num)
num=check([inp[0][2],inp[1][1],inp[2][0]])
if num:
    total.add(num)


print(len(total))