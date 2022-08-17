# 연구소

# 0 : 빈칸, 1: 벽, 2:바이러스

from itertools import combinations
import sys
import copy
from collections import deque
input = sys.stdin.readline

dx, dy = [0,0,-1,1], [1,-1,0,0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
queue = deque()

def bfs():
    global result
    tmp = copy.deepcopy(graph)
    for n in range(N):
        for m in range(M):
            if tmp[n][m]==2:
                queue.append([n,m])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny]==0:
                    tmp[nx][ny] = 2
                    queue.append([nx,ny])
    
    cnt = 0
    for i in tmp:
        cnt+=i.count(0)
    result = max(result,cnt)


wall = []
for n in range(N):
    for m in range(M):
        if graph[n][m]==0 : wall.append([n,m])

for a,b,c in combinations(wall,3):
    graph[a[0]][a[1]], graph[b[0]][b[1]], graph[c[0]][c[1]] = 1,1,1
    bfs()
    graph[a[0]][a[1]], graph[b[0]][b[1]], graph[c[0]][c[1]] = 0,0,0

print(result)