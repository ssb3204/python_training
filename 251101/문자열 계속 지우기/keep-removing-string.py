A = input()
B = input()

# Please write your code here.
while(True):
    if B not in A:
        break
    
    if B in A:
        A=list(A)
        B=list(B)
        for i in range(len(A)-len(B)+1):
            if A[i:i+len(B)]==B:
                for _ in range(len(B)):
                    A.pop(i)
                break
    A = "".join(A)
    B = "".join(B)
    
print(A)