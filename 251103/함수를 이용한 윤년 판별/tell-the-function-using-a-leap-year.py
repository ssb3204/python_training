y = int(input())

# Please write your code here.
def f(a):
    if a%100==0 and a%400!=0:
        return False
    elif a%4==0:
        return True
    else:
        return False

if f(y):
    print("true")
else:
    print("false")