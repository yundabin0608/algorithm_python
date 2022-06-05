# 퇴사

# 오늘부터 N+1 일째 되는 날 퇴사하기 위해 남은 N일 동안 최대한 많은 상담 할 것
# 하루에 하나씩 서로 다른 상담을 잡았음
# 각 상담은 완료하는데 걸리는 시간 T와 상담후 받을 수 있는 금액 P로 이뤄짐
# 상담을 적절히 골라 잡아 최대 수익 얻도록 할 것

# 테이블 맨 뒤에서부터 차근차근 더해나가는 형식

import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
dp=[0]*(N+1) 

for i in range(N-1,-1,-1):
    # 예로 7일까진데 7일에 2일짜리 일 못하니까 조건으로 막아둠
    if i+table[i][0]<=N:
        dp[i] = max(dp[i+1], table[i][1]+dp[i+table[i][0]])
    else: dp[i]=dp[i+1] 
    #dp[i]=0 은 안돼 왜냐면 6일차는 일 못하는데 7일차가 하면 6일차에 0이 아니라 7일꺼를 적어야 하니까

print(dp[0])