# 동전1

# n가지 동전, 각각의 가치는 다름 -> 이들로 합k 원이 되게하는 경우의 수 구하기
# 동전은 몇개든 사용 가능하며, n(1~100) k(1~10000)
# 경우의 수 출력 (2^31보단 작음)

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()

# dp[K]는 K원이 되는 경우의 수. dp[0]이란건 동전 하나만 쓰일때를 의미하는것
dp = [0]*(K+1) 
dp[0] = 1


# 예로 dp[6]이고 동전이 2이다? 그럼 dp[4]+1 인것 4원 만드는 방법에다가 2원만 넣어주면 되는것.
for c in coins:
    for i in range(c, K+1):
        dp[i] += dp[i-c]
print(dp[-1])

