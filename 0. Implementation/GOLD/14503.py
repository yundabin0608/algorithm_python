# 로봇청소기

# 로봇 청소기가 청소하는 영역의 수
# 북 동 남 서 (0 1 2 3)
# 왼방향 회전 : 0>3, 1>0 2>1 3>2 즉 (d+3)%4
# 후진 : 좌표에서 내 방향 빼주기

import sys
input = sys.stdin.readline
from collections import deque

dr, dc = [-1,0,1,0], [0,1,0,-1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

visited[r][c] = 1
result = 1

while True:
    flag = 0
    
    for _ in range(4):
        d = (d+3)%4
        nr, nc = r+dr[d], c+dc[d]

        if 0<=nr<N and 0<=nc<M and graph[nr][nc]==0 and visited[nr][nc]==0:
            visited[nr][nc]=1
            result +=1
            r,c,flag = nr,nc,1
            break
    
    # 즉 회전 못한경우, 후진시 벽일경우 끝
    if flag == 0:
        if graph[r-dr[d]][c-dc[d]] == 1:
            print(result)
            break
        else:
            r,c = r-dr[d], c-dc[d]