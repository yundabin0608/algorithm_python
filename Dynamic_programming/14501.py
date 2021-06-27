# 퇴사문제
# N+1일째 되는날 퇴사하려 N일동안 최대수로 상담진행
# 하루 하나씩 서로 다른사람 상담. 상담 완료 기간T, 상담 받을경우 받는 금액P
# 최대수익구하기. 

N=int(input())
T=[0]*N
P=[0]*N
dp=[0]*(N+1)

for i in range(N):
    a,b=map(int, input().split())
    T[i]=a
    P[i]=b

for i in range(N-1, -1, -1):
    if T[i]+i <= N:
        dp[i]=max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i]=dp[i+1]

print(dp[0])
