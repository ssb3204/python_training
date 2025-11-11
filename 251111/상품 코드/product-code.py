product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class std:
    def __init__(self,name="codetree",code=50):
        self.name=name
        self.code=code

C=std()
print(f"product {C.code} is {C.name}")
C=std(product_name,product_code)
print(f"product {C.code} is {C.name}")