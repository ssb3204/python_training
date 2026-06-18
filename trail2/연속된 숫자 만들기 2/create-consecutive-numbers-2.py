pos = list(map(int, input().split()))

def in_order():
    ls=pos.copy()
    ls.sort()
    if ls[0]+1 ==ls[1] and ls[1]+1 ==ls[2]:
        return True
    else:
        return False

# Please write your code here.

if in_order():
    print("0")
elif pos[0]+1 == pos [1]:
    if abs(pos[1]-pos[2]) >2:
        print("2")
    else:
        print("1")
elif pos[1]+1==pos[2]:
    if abs(pos[0]-pos[1])>2:
        print("2")
    else:
        print("1")
else:
    if abs(pos[0]-pos[1])>abs(pos[1]-pos[2]):
        if abs(pos[1]-pos[2])>2:
            print("2")
        else:
            print("1")
    else:
        if abs(pos[0]-pos[1])>2:
            print("2")
        else:
            print("1")