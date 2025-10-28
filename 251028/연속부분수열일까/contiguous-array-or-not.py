a,b=map(int,input().split())

la=list(map(int,input().split()))
lb=list(map(int,input().split()))
is_in=False

if a>b:
    for i in range(len(la)-len(lb)+1):
        sa=la[i:len(lb)+i]
        if sa==lb:
            is_in=True
else:
    for i in range(len(lb)-len(la)+1):
        sb=lb[i:len(la)+i]
        if sb==la:
            is_in=True

if is_in:
    print("Yes")
else:
    print("No")

