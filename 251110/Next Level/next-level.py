user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Std:
    def __init__(self, id="codetree", lev=10):
        self.id=id
        self.lev=lev

C=Std()
print(f"user {C.id} lv {C.lev}")

C=Std(id="hello",lev=28)
print(f"user {C.id} lv {C.lev}")