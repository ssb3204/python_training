a=int(input())
is_t=True

for i in range(2,a):
    if a%i==0:
        is_t=False

if is_t:
    print("P")
else:
    print("C")