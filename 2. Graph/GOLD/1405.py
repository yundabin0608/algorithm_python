# 미친 로봇

# 로봇이 N번 행동을 취함. 이때 로봇은 4방향중 하나로 이동하며
# 로봇이 같은 곳을 한번보다 많이 이동하지 않으면 이동경로 단순
# e: 동, w: 서, n: 북, s: 남 (100~0), Ndms 14보다 작거나 같은 자연수
# 출력은 로봇의 이동 경로가 단순할 확률

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #dfs 깊이 제한

N, e, w, s, n = map(int, input().split())
possibility = [e/100, w/100, s/100, n/100]
result = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]

# 로봇 있는자리 + 양옆으로 N이동할 정도범위, 로봇은 N,N 위치
graph = [[0]*(2*N+1) for _ in range(2*N+1)]

# 로봇이 같은곳을 한번보다 많이 이동하지 않으면 됨 => 갔던 곳 다시 안가면 됨
def dfs(x,y,count):
    if count==N:    
        return 1
    graph[y][x] =1  # 이동시 1로 방문했음 표시
    tmp = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if graph[ny][nx] == 0: #방문하지 않았다면
            tmp += dfs(nx,ny,count+1)*possibility[i]
    # 경우의 수 여러번 구하니까 다 구한 후엔 방문지점 지워줄 것
    graph[y][x]=0 
    return tmp
print(dfs(N,N,0))