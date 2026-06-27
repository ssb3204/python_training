ability = list(map(int, input().split()))

ability.sort()
# Please write your code here.
a=ability[0]+ability[5]
b=ability[1]+ability[4]
c=ability[2]+ability[3]

max_num=max(a,max(b,c))
min_num=min(a,min(b,c))

print(max_num-min_num)
