Y, M, D = map(int, input().split())

# Please write your code here.
def yoon(a):
    if a%4==0 and a%100==0 and a%400==0:
        return 1
    elif a%4==0 and a%100!=0:
        return 1
    else:
        return 0
    

def sesson(b):
    if b in [3,4,5]:
        print("Spring")
    elif b in [6,7,8]:
        print("Summer")
    elif b in [9,10,11]:
        print("Fall")
    elif b in [12,1,2]:
        print("Winter")

def ex(a,b,c):
    if b in [1,3,5,7,8,10,12]:
        if c<=31:
            return True
        else:
            return False
    elif b==2:
        if yoon(a):
            if c<=29:
                return True
            else:
                return False
        else:
            if c<=28:
                return True
            else:
                return False
    elif b in [4,6,9,11]:
        if c<=30:
            return True
        else:
            return False
    else:
        return False

if ex(Y,M,D):
    sesson(M)
else:
    print("-1")

