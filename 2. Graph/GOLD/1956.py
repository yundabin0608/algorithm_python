# 운동

# V(2~400)개 마을과 E개 도로로 구성된 도시, 도로는 단방향
# 도로의 정보가 주어졌을때, 도로 길이 합이 최소인 사이클 찾는 프로그램 작성, 두마을 왕복도 사이클임

import sys
input = sys.stdin.readline
INF = int(1e9)

V,E = map(int, input().split())
road = [[INF]*V for _ in range(V)]
result = -1
for _ in range(E):
    a,b,c = map(int, input().split())
    road[a-1][b-1] = c

# 플루이드 와샬 사이클도 포함하므로 다음과 같이 수행
for k in range(V):
    for i in range(V):
        for j in range(V):
            road[i][j] = min(road[i][j], road[i][k]+road[k][j])

# 각 배열의 i=j 인 부분만 보면 되므로 이중포문 필요X
result = INF
for i in range(V):
    result = min(result, road[i][i])
print(-1 if result ==INF else result)