# 병사 배치하기
# 병사 전투력 오름차순이 되도록 할때 남은 병사수가 최대 되도록 하기

N=int(input())
power=list(map(int,input().split()))
dp=[1]*N

for i in range(1,N):
    for j in range(0,i):
        if power[j] > power[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(N-max(dp))