# 동전1

# n가지 동전, 각각의 가치는 다름 이들을 사용해 합k 원이 되게하는 경우의 수 구하기
# 동전은 몇개라도 쓸 수 있음
# 입력 n(1~100) k(1~10000), n줄만큼 동전의 가치 주어짐
# 첫줄에 경우의 수 출력 2^31보단 작을 것

n, k = map(int,input().split())
coin = []
dp = [0 for i in range(k+1)]
dp[0]=1

for i in range(n):
    coin.append(int(input()))
coin.sort()

for i in coin:
    for j in range(i, k+1):
        if j>=i:
            dp[j]+=dp[j-i]
print(dp[k])

# 1,2원 사용시 예로 dp[5]=dp[5]+dp[3] 라면
# dp[5]=1+1+1+1+1 & dp[3]=1+1+1 & 1+2 
# 즉 dp[3]은 자기 동전1개인 2원+1+1+1 or 2원+2+1 총 3가지

# 1,2,5 원 사용시 예로 dp[5]=dp[5]+dp[0]
# dp[5]=1+1+1+1+1 & 1+1+1+2 & 1+2+2 & dp[0]=1
# 즉 dp[0]은 5원짜리 동전 1개를 사용한다는 의미 => 총 4가지
