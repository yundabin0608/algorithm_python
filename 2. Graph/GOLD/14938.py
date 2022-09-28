# 서강 그라운드

# 각 지역은 일정한 길이(l:1~15)의 길로 다른 지역과 연결되었으며 양방향 통행이 가능
# 낙하한 지역 중심으로 수색 범위 m(1~15) 이내 모든 지역 아이템 습득 가능

import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int, input().split())
items = list(map(int, input().split()))
roads = [[INF]*n for _ in range(n)]
for _ in range(r):
    a,b,l = map(int, input().split())
    roads[a-1][b-1] = l
    roads[b-1][a-1] = l

# 플루이드 와샬 수행 (최단거리 갱신)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j : roads[i][j]=0
            else : roads[i][j]= min(roads[i][j], roads[i][k] + roads[k][j])

# 각 i->j 인 길의 길이를 road에 넣어두고 m이하면 모두 더함
# i -> [1,2,3,4,5] 탐색 i는 시작노드라는 뜻 (이들끼리도 비교 필요)
result = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if roads[i][j]<=m:
            tmp += items[j]
    result = max(result, tmp)
print(result)