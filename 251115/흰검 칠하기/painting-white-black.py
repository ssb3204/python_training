n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

MAX = 200050
ls = [[0, "none"] for _ in range(MAX)]
now = MAX // 2

for i in range(n):
    a = int(x[i])
    b = dir[i]
    if b == "R":
        for j in range(now, now + a):
            ls[j][0] += 1
            ls[j][1] = "black"
        now = now + a
    else:
        for j in range(now, now - a, -1):
            ls[j][0] += 1
            ls[j][1] = "white"
        now = now - a

b = w = g = 0
for cnt, color in ls:
    if color == "none" or cnt == 0:
        continue
    if cnt >= 4:
        g += 1
    elif color == "black":
        b += 1
    elif color == "white":
        w += 1

print(w, b, g, sep=" ")
