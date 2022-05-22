# 적록색약

# 적록색약은 빨, 초의 차이를 거의 못느낌
# 그림은 R,G,B로 색칠되어 있고 여러 구역이며 한 구역은 같은색이다
# 같은 색상이 상하좌우로 인접하면 같은구역이고 색상차를 못느끼면 같은색으로 간주
# 적록색약인 사람이 봤을때와 아닌 사람이 볼때 구역의 수를 구할것

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
color = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans1, ans2 = 0, 0
dx, dy = [-1,1,0,0], [0,0,-1,1]

def dfs(x,y):
    
    rgb = color[y][x]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and visited[ny][nx]==False and color[ny][nx] == rgb:
            visited[ny][nx] = True
            dfs(nx,ny)

for y in range(N):
    for x in range(N):
        if visited[y][x]==False:
            dfs(x,y)
            ans1 += 1

# 적록색맹이므로 G->R로 변환후 수행
for i in range(N):
    for j in range(N):
        if color[i][j]=='G': color[i][j]='R'

visited = [[False] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            dfs(x,y)
            ans2 += 1

print(ans1, ans2)