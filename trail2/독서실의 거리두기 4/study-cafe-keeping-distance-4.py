N = int(input())
seat = input()

# Please write your code here.
seats=list(seat)

def min_dis(arr):
    l=[]
    start=-1
    for i in range(N):
        if arr[i]=='1':
            if start!=-1:
                l.append(i-start)
            start=i
    return min(l)


min_nums=[]
for i in range(N):
    if seats[i]=='1':
        continue
    ls=seats.copy()
    ls[i]='1'
    for j in range(i+1,N):
        if ls[j]=='1':
            continue
        ls2=ls.copy()
        ls2[j]='1'
        min_nums.append(min_dis(ls2))

print(max(min_nums))