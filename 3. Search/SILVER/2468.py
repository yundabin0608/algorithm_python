# 안전영역

# 지역의 높이정보 파악 후 비가 내렸을때 비에 잠기지 않는 영역이 최대로 몇개인지 조사

import sys
input =sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

def dfs(x, y, h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny < N) and arr[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, h)

for h in range(max(map(max, arr))):  
    num = 0
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visited[i][j] == 0:
                visited[i][j] = 1
                num += 1
                dfs(i, j, h)
    result = max(result, num)

print(result)