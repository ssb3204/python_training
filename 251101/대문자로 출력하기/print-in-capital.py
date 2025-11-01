a=input()

for i in a:
    i=ord(i)
    if i>=65 and 122>=i:
        print(chr(i).upper(),end="")