a=input()
b=input()
num1=[]
num2=[]
for i in a:
    if i.isdigit():
        num1.append(i)


for i in b:
    if i.isdigit():
        num2.append(i)

n="".join(num1)
m="".join(num2)
print(int(n)+int(m))