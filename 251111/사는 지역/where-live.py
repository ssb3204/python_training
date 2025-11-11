n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class std:
    def __init__(self,name,street,region):
        self.name=name
        self.street=street
        self.region=region


ls=[]
for i in range(n):
    ls.append(std(name[i],street_address[i],region[i]))

ls.sort(key=lambda x:name)

print(f"name {ls[n-1].name}")
print(f"addr {ls[n-1].street}")
print(f"city {ls[n-1].region}")