Y, M, D = map(int, input().split())

# Please write your code here.
def yoon(a):
    if a%100 and a%400!=0:
        return 1
    elif a%4==0:
        if a%100!=0:
            return 0
        else:
            return 1
    

def sesson(b):
    if b>=3 and 5>=b:
        print("Spring")
    elif b>=6 and 8>=b:
        print("Summer")
    elif b>=9 and 11>=b:
        print("Fall")
    else:
        print("Winter")

def ex(a,b):
    if a in [1,3,5,7,8,10,12]:
        if b<=31:
            return True
        else:
            return False
    elif a==2:
        if yoon(a):
            if b<=29:
                return True
            else:
                return False
        else:
            if b<=28:
                return True
            else:
                return False
    elif a in [2,4,6,9,11]:
        if b<=30:
            return True
        else:
            return False
    else:
        return False

if ex(M,D):
    sesson(M)
else:
    print("-1")

