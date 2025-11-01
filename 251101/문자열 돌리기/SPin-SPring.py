a=input()

for _ in range(len(a)+1):
    print(a)
    c=a[-1:]
    b=a[:-1]
    a=c+b
    