n = int(input())
S = input()
cnt=0
# Please write your code here.
for i in range(len(S)):
    fir = S[i]
    if fir =='C':
        for j in range(i+1,len(S)):
            sec= S[j]
            if sec=='O':
                for k in range(j+1,len(S)):
                    thr=S[k]
                    if thr=='W':
                        cnt+=1

print(cnt)