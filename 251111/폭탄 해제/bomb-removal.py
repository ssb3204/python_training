unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class std:
    def __init__(self,code,color,second):
        self.code=code
        self.color=color
        self.second=second

C=std(unlock_code, wire_color, seconds)
print(f"code : {C.code}")
print(f"color : {C.color}")
print(f"second : {C.second}")