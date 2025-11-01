a=input()
cnt=0
for i in a:
    if i.isdigit():
        cnt+=int(i)
print(cnt)