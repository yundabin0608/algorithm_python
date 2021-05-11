# 정수 삼각형
# 위에서부터 시작해 아래 있는 수를 선택해 밑으로 내려 올때 합 최대

N=int(input())

triangle_dp=[]
for i in range(N):
    triangle_dp.append(list(map(int, input().split()))+[-1]*(N-i-1))

for j in range(1,N):
    for i in range(N):
        if triangle_dp[j][i] >=0:
            if i==0:
                left_down=0
            else:
                left_down=triangle_dp[j-1][i-1]
            if j==i:
                down=0
            else:
                down=triangle_dp[j-1][i]

            triangle_dp[j][i]=triangle_dp[j][i]+max(left_down,down)

print(max(triangle_dp[N-1]))
