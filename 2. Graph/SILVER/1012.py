# 유기농 배추

# 배추흰지렁이 필요 갯수 찾기  => 이어진 배추구역이 몇개 인지 찾기
# 기존의 입력된 그래프가 값이 0보다 크면 dfs를 모두 호출하고 그에 이어진것들을 재귀로 호출하면서 좌표들을 모두 -1로 바꾸는 방식에서
# 기존의 dfs는 dy dx를 탐색하면서 1이면 다시 재귀하도록 했는데
# 현재 코드는 dfs에서 1인지 확인 후 dy, dx를 탐색하도록 하면서 좀더 시간을 단축하도록 함

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

T =int(input())
for _ in range(T):
    M,N,K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
        
    def dfs(x, y):
        
        if graph[y][x]==1:
            # 그자리 지나갔으므로 0으로 바꾸고 상하좌우 탐색
            graph[y][x]=-1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<M and 0<=ny<N and graph[ny][nx]==1:
                    dfs(nx, ny)
                    
    count=0
    for n in range(N):
        for m in range(M):
            if graph[n][m]==1:
                dfs(m,n)
                count+=1
            
    print(count)
    
    