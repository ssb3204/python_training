x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
left_x=min(min(x1,x2),min(a1,a2))
left_y=min(min(y1,y2),min(b1,b2))

right_x=max(max(x1,x2),max(a1,a2))
right_y=max(max(y1,y2),max(b1,b2))

print(abs(left_x-right_x)*abs(left_y-right_y))