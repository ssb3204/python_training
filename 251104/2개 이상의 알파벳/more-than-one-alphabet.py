A = input()

# Please write your code here.
def f(a):
    for i in range(1,len(a)+1):
        for j in range(len(a)-i):
            if a[i]!=a[j]:
                return True
            else:
                return False

print("Yes" if f(A) else "No")

