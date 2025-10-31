ls=[]
for _ in range(10):
    a=input()
    ls.append(a)

a=input()
is_t=False
for i in ls:
    if i.endswith(a):
        is_t=True

if is_t!:
    print("None")