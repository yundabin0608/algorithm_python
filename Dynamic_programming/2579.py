# 계단 오르기
# 마찬가지로 계단을 +1 또는 +2 해서 오를 수 있는데 연속된 세계단밟기는 불가하다는게 특징 즉 +1+1 이면 +2할것
# 마지막 계단은 무조건 밟아야 하므로 마지막에서 시작하자

N=int(input())
stairs=[]
for i in range(N):
    stairs.append(int(input()))

dp=[0]*300

if N==1:
    print(stairs[0])
elif N==2:
    print(stairs[0]+stairs[1])
elif N==3:
    print(max(stairs[0],stairs[1])+stairs[2])
elif N==4:
    print(stairs[0]+max(stairs[1],stairs[2])+stairs[3])

else:
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0],stairs[1])+stairs[2]
    dp[3]=stairs[0]+max(stairs[1],stairs[2])+stairs[3]

    for i in range(3,N):
        dp[i]=max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1])

    print(dp[N-1])