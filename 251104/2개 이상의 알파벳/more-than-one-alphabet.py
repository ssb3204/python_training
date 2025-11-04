A = input()

# Please write your code here.
def f(a):
    is_t=False
    for i in range(len(a)-2):
        for j in range(i+1,len(a)):
            if a[i]!=a[j]:
                is_t=True
    if is_t:
        return True
    else:
        return False

print("Yes" if f(A) else "No")

