a=input()

for i in a:
    if i.isupper():
        print(i.lower(),end="")
    elif i.islower():
        print(i.upper(),end="")