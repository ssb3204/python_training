ls=[]
for _ in range(10):
    a=input()
    ls.append(a)

a=input()
is_t=False
print(a)
for i in ls:
    if i.endswith(a):
        is_t=True
        print(i)

if is_t==False:
    print("None")