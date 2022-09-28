# 플로이드

# n개의 도시(2~100), m개의 버스 (1~100,000)
# 모든 도시의 상에 대해 A->B 인 최소값 구하기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9) 
cost = [ [INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    # 입력으로 들어온 비용이 더 작다면 갱신
    if cost[a][b]>c: cost[a][b]=c 

# 경유하는게 더 저렴하면 경유한 값으로 변경
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j and cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]

for i in cost[1:]:
    for j in i[1:] :
        print(j if j!=INF else 0, end=" ")
    print()