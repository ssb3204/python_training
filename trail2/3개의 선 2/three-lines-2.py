n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

def line(xy):
    return ('x', x[xy]) if xy <n else ('y',y[xy-n])

found=False
for i in range(2*n):
    for j in range(i+1,2*n):
        for k in range(j+1,2*n):
            remain=points
            for a,b in (line(i),line(j),line(k)):
                if a=='x':
                    remain = [p for p in remain if p[0]!=b]
                else:
                    remain =[p for p in remain if p[1]!=b] 
            if not remain:
                found=True
                break
        if found:
            break
    if found:
        break

print('1' if found else '0')