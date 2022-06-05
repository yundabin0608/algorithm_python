# 피보나치 함수

# 예로 fibo(3) 은 fibo(2)와 fibo(1)을 호출하고
# fibo(2)느 fibo(1)과 fibo(0)을 호출
# fibo(1)은 1을 출력하고 1을 리턴. fibo(0)은 0을 출력하고 리턴
# 즉 fibo(2) = 1+0 = 1 , fibo(3) = 1+1 = 2

# fibo(N) 호출시 0과 1이 몇번 호출되는가?

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    if N==0 : print("1 0")
    elif N==1 : print("0 1")
    else:
        # fibo(0)과 fibo(1)의 표현
        dp = [[1,0],[0,1]]
        for i in range(2,N+1):
            dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
        
        print(dp[N][0], dp[N][1])