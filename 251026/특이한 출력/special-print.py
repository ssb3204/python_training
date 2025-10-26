a=int(input())

for i in range(1,a+1):
    for j in range(1,a+1):
        print(f"({i}, {j})",end=" ")
        if (i+j)%4==0:
            print()
            continue