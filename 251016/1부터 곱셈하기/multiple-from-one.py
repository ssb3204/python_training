a=int(input())
num=1
for i in range(1,11):
    num*=i
    if num>=a:
        print(i)
        break