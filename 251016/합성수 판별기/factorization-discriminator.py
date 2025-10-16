a=int(input())

is_t=False

for i in range(2,a):
    if a%i==0:
        is_t=True

if is_t:
    print("C")
else:
    print("N")