x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
x=[x1,x2,a1,a2]
y=[y1,y2,b1,b2]

x=max(x)-min(x)
y=max(y)-min(y)

num=max(x,y)

print(num**2)