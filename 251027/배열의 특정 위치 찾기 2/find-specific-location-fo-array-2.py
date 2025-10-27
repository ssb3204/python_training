ls=list(map(int,input().split()))
even=0
odd=0
for i in range(1,11):
    if i%2==0:
        even+=ls[i-1]
    else:
        odd+=ls[i-1]

if even>odd:
    print(even-odd)
else:
    print(odd-even)