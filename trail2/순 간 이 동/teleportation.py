a, b, x, y = map(int, input().split())

# Please write your code here.

if abs(a-b)>abs(a-x)+abs(b-y): 
    print(abs(a-x)+abs(b-y))
elif abs(a-b)>abs(a-y)+abs(b-x):
    print(abs(a-y)+abs(b-x))
else:
    print(abs(a-b))