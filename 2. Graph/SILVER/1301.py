# 전투 - 정답자들은 dfs가 시간 빨리 나오는느낌이었음 dfs로도 해봐

# N명 뭉쳤을때, N^2위력을 낸다. 상하좌우 붙는 경우 인접했다고 봄
# 당신의 병사의 위력의 합과 적국 병사의 위력의 합을 출력 w우리팀 b상대팀
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
warriors = []
for _ in range(M):
    warriors.append(list(input()))
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(n,m,team):
    queue = deque()
    queue.append((n,m))
    count=0
    warriors[m][n]==0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if warriors[ny][nx] !=0 and warriors[ny][nx] == team:
                    queue.append((nx,ny))
                    warriors[ny][nx]=0
                    count+=1
    return (1 if count ==0 else count)**2

blue, white = 0,0
for y in range(M):
    for x in range(N):
        if warriors[y][x]!=0:
            if warriors[y][x] == "W":
                white+=bfs(x,y,"W")
            else:
                blue+=bfs(x,y,"B")
print(white, blue)