secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Std:
    def __init__(self, a , b, c):
        self.a=a
        self.b=b
        self.c=c

C=Std(secret_code, meeting_point, time)

print(f"secret code : {C.a}")
print(f"meeting point : {C.b}")
print(f"time : {C.c}")