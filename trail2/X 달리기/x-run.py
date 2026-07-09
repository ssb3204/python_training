X = int(input())

# Please write your code here.
cnt=0
speed=1
remain=X-1
dis=1


while(speed>0):
    num=0
    cnt+=1
    for i in range(speed,0,-1):
        num+=i

    if remain-(speed+1) >=num:
        speed+=1
    elif remain-speed>= num-speed:
        pass
    else:
        speed-=1
    remain-=speed


print(cnt)