# 포도주 시식

# 연속으로 놓인 포도주 3잔을 모두 마실수는 없으며 선택시 모두마신뒤 제자리
# 최대로 마실수 있는 포도주 최대 양 출력

import sys
input = sys.stdin.readline

N = int(input())
# 포도주는 일렬로 놓임 1~10000
drink, dp = [0]*(N+1), [0]*(N+1)

for i in range(N):
    drink[i] = int(input())

dp[0] = drink[0]
dp[1] = drink[0] + drink[1]

for i in range(2,N):
    #  ~~X 와  ~XO 와  ~XOO 중 최대 
    dp[i] = max(dp[i-1], dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])
    # dp[음수]여도 (즉 i=1, dp[-1]=0) 맨 뒤쪽 dp가 0이므로 영향을 안미치게된다.

print(dp[N-1])
