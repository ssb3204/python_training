MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class std:
    def __init__(self, codename,score):
        self.codename=codename
        self.score=score

code=[]
for i in range(MAX_N):
    code.append(std(codenames[i],scores[i]))


code.sort(key=lambda x: x.score)
print(code[0].codename,code[0].score,sep=" ")