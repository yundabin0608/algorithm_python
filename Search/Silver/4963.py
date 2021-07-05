# 섬의 개수 
# 가로 세로 대각선 연결 = 경로가 있는 섬
# 00이 나올때까지 입력은 계속 반복, 지도너비 w,h , 바다=0, 땅=1

# 가장 먼저 생각한건 dfs

import sys
sys.setrecursionlimit(50000)
### 런타임 에러 해결을 위해 recursionlimit을 정해주어야함 ###
def dfs(x,y):
    dx=[-1,1,-1,0,1,-1,0,1]
    dy=[0,0,1,1,1,-1,-1,-1]

    matrix[y][x]=0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if (0<=nx<w) and (0<=ny<h):
            if matrix[ny][nx]==1:
                matrix[ny][nx]=0
                dfs(nx, ny)

while True:
    w,h= map(int,input().split())
    
    if w==0 & h==0 : break

    matrix = []
    for i in range(h):
        matrix.append(list(map(int, input().split())))

    count=0
    for i in range(h):
        for j in range(w):
            if matrix[i][j]==1:
                dfs(j,i)
                count+=1
    print(count)

# How-to BFS ------------------------------------
# from collections import deque
# import sys
# read = sys.stdin.readline

# def bfs(x, y):
#   dx = [1, -1, 0, 0, 1, -1, 1, -1]
#   dy = [0, 0, -1, 1, -1, 1, 1, -1]

#   matrix[x][y] = 0
#   q = deque()
#   q.append([x, y])

#   while q:
#     a, b = q.popleft()
#     for i in range(8):
#       nx, ny = a + dx[i],  b + dy[i]
#       if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 1:
#         matrix[nx][ny] = 0
#         q.append([nx, ny])

# while True:
#   w, h = map(int, input().split())
#   if w == 0 & h == 0: break
#   matrix = []

#   for _ in range(h):
#     matrix.append(list(map(int, input().split())))

#   count = 0
#   for i in range(h):
#     for j in range(w):
#       if matrix[i][j] == 1:
#         bfs(i, j)
#         count += 1
#   print(count)