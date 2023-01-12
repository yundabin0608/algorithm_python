# 가장 긴 증가하는 부분수열 4

# 수열 A가 주어질때, 긴 증가하는 부분수열 길이를 구하고 그 수열을 구할 것

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
answer = []

# 배열 길이만큼 도는데 해당 원소 전 원소까지 돌것. 해당 원소가 전 원소보다 크면 dp
for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[i], dp[j]+1)

maxlen = max(dp)
print(maxlen)

for i in range(N-1, -1, -1):
    if dp[i] == maxlen:
        answer.append(A[i])
        maxlen -= 1
answer.reverse()
print(*answer)

# 예로 [10, 20, 10, 30, 20, 50]
# dp는 [1, 2, 1, 3, 2, 4] 저장되니까
# 이중   *  *     *     *  이것만 따서 배열 