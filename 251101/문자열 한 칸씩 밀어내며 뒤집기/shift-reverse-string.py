input_str, q = input().split()
input_str= list(input_str)
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for i in queries:
    if i==1:
        c=input_str[:1]
        b=input_str[1:]
        input_str=b+c
    elif i==2:
        c=input_str[-1:]
        b=input_str[:-1]
        input_str=c+b
    else:
        input_str.reverse()
    
    for i in input_str:
        print(i,end="")
    print()

