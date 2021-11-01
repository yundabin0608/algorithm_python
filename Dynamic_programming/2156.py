# 포도주 시식

# 포도주 시식 (포도주는 일렬로 놓임 1~n(<=10000)번, 양이 써있음 (1000이하 음의 정수))
# 1) 포도주 잔 선택시 그잔은 모두 마셔야하며 원래 자리에 둘것.
# 2) 연속으로 놓인 포도주 3잔을 모두 마실수는 없음
# 출력 : 최대한으로 마실 수 있는 포도주의 양

# dp와 drink를 10000과 같이 제한을 안주니까 정답이 한 70%까지 오르다가 런타임 에러가 났었음

N = int(input())
drink = [0]*10000
dp=[0]*10000

for i in range(N):
    drink[i] = int(input())

dp[0] = drink[0]
dp[1] = drink[0]+drink[1]
dp[2] = max(dp[1], drink[0]+drink[2], drink[1]+drink[2])

for i in range(3,N):
    dp[i] = max(dp[i-1], dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])

print(dp)


# 6 | 10 | 13 | 9 | 8 | 1
# dp[0]=6   (6) 
# dp[1]=16  (6+10) => dp[0]+d[1]
# dp[2]=23  (10+13) => dp[1] or dp[0]+d[2] or d[1]+d[2]
# dp[3]= 28 (6+13+9) => dp[2] or dp[1]+d[4] or dp[0]+ dp[3]+d[4]
# dp[4]=33  (6+10+9+8)
# dp[5]=33  (6+10+9+8)
# => 점화식 dp[K] = max(dp[k-1], dp[k-3]+drink[k-1]+drink[k], dp[k-2], drink[i])