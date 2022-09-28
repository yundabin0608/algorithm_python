# 플로이드2
# 11404에 거쳐가는 도시개수와 경로 추가한 문제

import sys
input = sys.stdin.readline
INF = int(1e9) 

n = int(input())
m = int(input())
path = [[[] for _ in range(n+1)] for _ in range(n+1)]  
cost = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    if cost[a][b]>c: cost[a][b]=c 
    path[a][b] = [a,b]

# 플루이드 
for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i != j:
				if cost[i][j] > cost[i][k] + cost[k][j]:
					cost[i][j] = cost[i][k] + cost[k][j]
					path[i][j] = path[i][k] + path[k][j][1:]
                    # 예로 2>4 인데 2>3>4 로 바뀌는 상황
                    # 2>3 : 2>1>3, 3>4 : 3>5>4 이면, 2>1>3 + 3>5>4

# 도시 i에서 j로 가는데 필요한 최소 비용 못가면 0
for i in cost[1:]:
    for j in i[1:]: 
        print(j if j!=INF else 0, end=" ")
    print()
# 도시 i>j 로 가는 최소 비용에 포함된 도시의 개수 k & 경로 출력 (dist, path)
for i in range(1, n+1):
	for j in range(1, n+1):
		if cost[i][j] == INF or i == j: print(0)
		else: print(len(path[i][j]), *path[i][j])