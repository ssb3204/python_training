N = int(input())
seat = input()
ls = list(seat)

vals = []
for i in range(N):
    if ls[i] != '0':
        continue

    lst = ls.copy()
    lst[i] = '1' 

    ones = []
    for j in range(N):
        if lst[j] == '1':
            ones.append(j)

    min_gap = N
    for k in range(len(ones) - 1):
        gap = ones[k+1] - ones[k]
        if gap < min_gap:
            min_gap = gap

    vals.append(min_gap)

print(max(vals))