# 퇴사2

# N+1일 퇴사를 위해 N일동안 최대 상담할 것  (상담기간 Ti, 받는 금액 Pi)
# 첫줄 N(1~1500000), 둘째줄부터 N개줄에 Ti, Pi (1~50, 1~1000)
# 얻을 수 있는 최대 이익 출력

import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
dp = [0]*(N+1) # 인덱스번째 날까지 최대 금액

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t) 
    P.append(p)

for i in range(0,N):
    if T[i]<=N-i:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])