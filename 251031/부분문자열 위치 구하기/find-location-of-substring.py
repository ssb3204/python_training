input_str = input()
target_str = input()
num=-1
# Please write your code here.
for i in range(len(input_str)-1):
    if target_str==input_str[i:i+len(target_str)]:
        num=input_str.index(target_str)
    
print(num)
