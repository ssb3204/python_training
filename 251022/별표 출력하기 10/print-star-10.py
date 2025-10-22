a=int(input())

for i in range(1,2*a+1):
    if i%2==0:
        print("* " * (a-(i//2)+1),end=" ")
    else: 
        print("* " * ((i//2)+1),end=" ")
    print()