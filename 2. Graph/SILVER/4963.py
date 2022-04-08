# 섬의 개수

# 지도를 읽고 섬의 갯수 세기
# 가로,세로, 대각전의 경우 갈 수 있는 섬 => 이렇게 이어진게 하나의 섬

import sys
from collections import deque
input = sys.stdin.readline

# 동북, 동, 동남, 북, 남, 서북, 서, 서남 쪽 
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
answer = []

def bfs(i,j):
    #visited = [[0]*w for _ in range(h)]
    queue = deque()
    queue.append([j,i])
    #visited[i][j] = 1
    maps[i][j] == 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<w and 0<=ny<h and maps[ny][nx]==1: # n과 h 함수인자로 넣어줘야하나?
                maps[ny][nx]=0
                queue.append([nx, ny])
    

while(1):
    
    w,h = map(int, input().split())
    result = 0
    if w==0 and h==0 : break
    
    maps = [list(map(int, input().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i,j)
                result+=1
                
    answer.append(result)
    
print(*answer, sep="\n") 
# *answer시 한줄에 띄어쓰기로 구분되어 모두 출력되는데
# sep으로 띄어쓰기 대신 줄바꿈을 넣어줄 수 있음