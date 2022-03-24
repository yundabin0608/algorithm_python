# 미로탐색

# 1: 이동 가능 0: 이동불가 (1,1)에서 출발후 (N,M)으로 갈때 최소칸 수
# 항상 도착할 수 있는 경우만 입력으로 주어짐

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
miro = []
visited = [[0]*M for _ in range(N)]
count = 0

for _ in range(N): # 입력시 맨 끝 줄바꿈 문자는 제외 
    miro.append(list(map(int,input().rstrip())))
    
# 갈림길이 있을 수도 있으니 bfs 로 하자. bfs는 이동칸수를 반환

queue = deque()
queue.append((0,0))
visited[0][0]=1

while queue:
    x, y = queue.popleft()
    if x == M-1 and y==N-1:
        print(visited[y][x])
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N and miro[ny][nx]==1 and visited[ny][nx]==0:
            # nx, ny 가 범위내에 존재하고 방문한적 없는 이동 방문 칸
            # 방문표시 후 현좌표: cnt 다음좌표: cnt+1
            visited[ny][nx]=visited[y][x]+1
            queue.append((nx,ny))
    

    
    
    