import sys
arr = list(map(int, input().split()))

# Please write your code here.
all_same=[]

def team(i,j,k,x):
    team1=arr[i]+arr[j]
    team2=arr[k]+arr[x]
    team3=sum(arr)-team1-team2

    if team1 != team2 and team2 != team3 and team3 != team1:

        max_team=max(team1,max(team2,team3))
        min_team=min(team1,min(team2,team3))

        min_num=max_team-min_team

        all_same.append("False")
        return min_num
    else:
        all_same.append("True")
        return -1

answer=sys.maxsize
for i in range(5):
    for j in range(i+1,5):
        for k in range(5):
            for x in range(k+1,5):
                if i==k or i==x or j==k or j==x:
                    continue
                num=team(i,j,k,x)
                if num!=-1:
                    answer=min(answer,num)

if "False" in all_same:
    print(answer)
else:
    print(-1)