# 동전2

# n가지 동전, 각각의 가치는 다름 -> 이들로 합k원이 되게하고 동전 최소개일때 동전수 구하기
# 동전은 몇개든 사용 가능하며, n(1~100) k(1~10000) 불가능할 경우 -1 출력

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

dp = [10001]*(K+1) # K원이 되게하는 동전 최소수. 동전이 10000개일때가 최대이므로 다음처럼 설정
dp[0]=0

for c in coins:
    for i in range(c, K+1):
        dp[i] = min(dp[i], dp[i-c]+1) # 예로 dp[7]이고 c=4 이면 (7-4)3원일때 최소수+1개

print(dp[-1]) if dp[-1]!=10001 else print("-1")