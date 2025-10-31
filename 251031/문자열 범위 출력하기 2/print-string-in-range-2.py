a=input()
b=int(input())
if b>=len(a):
    print(a[::-1])
else:
    print(a[len(a):len(a)-b-1:-1])