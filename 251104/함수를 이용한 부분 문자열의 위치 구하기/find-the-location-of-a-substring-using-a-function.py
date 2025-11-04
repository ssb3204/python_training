text = input()
pattern = input()

# Please write your code here.
def f(a,b):
    if b in a:
        return a.index(b)
    else:
        return -1

a=f(text,pattern)
print(a)