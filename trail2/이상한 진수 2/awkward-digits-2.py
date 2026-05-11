a = input()
total=0
flag=False
# Please write your code here.
for i in a:
    if i =='0':
        flag=True

if flag:
    for i in range(1,len(a)):
        if a[i]=='0':
            lst=list(a)
            lst[i]='1'
            a=''.join(lst)
            total=int(a,2)
            break
else:
    lst=list(a)
    lst[-1]='0'
    a=''.join(lst)
    total=int(a,2)
    
print(total)
        

        
        