# 정수삼각형

# 위에서부터 시작해 아래 있는 수를 선택해 밑으로 내려 올때 합 최대

import sys
input = sys.stdin.readline


dp=[]
N = int(input())
for i in range(N):
    dp.append(list(map(int, input().split()))+[-1]*(N-1-i))

# 7 -1 -1 -1 -1
# 3  8 -1 -1 -1
# 8  1  0 -1 -1
# 2  7  4  4 -1
# 4  5  2  6  5

for j in range(1,N):
    for i in range(N):
        if dp[j][i] >=0:
            if i==0:  left_down=0 # 벽에 붙어있어서 왼쪽 위에 값 -1이라 없음
            else:     left_down=dp[j-1][i-1]
            if j==i:  down=0      # 위쪽은 -1이라 없음
            else:     down=dp[j-1][i]

            dp[j][i]=dp[j][i]+max(left_down,down)

print(max(dp[N-1]))