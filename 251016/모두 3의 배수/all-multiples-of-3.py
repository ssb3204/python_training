a=[int(input()) for _ in range(5)]
is_t=True
for i in a:
    if i%3!=0:
        is_t=False

if is_t:
    print("1")
else:
    print("0")