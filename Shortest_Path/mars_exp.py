# 화성탐사
# 화성 탐사 기계가 존재 공간은 N x N의 2차원 공간, 각각의 칸을 지나기 위한 비용(에너지 소모량) 존재
# 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는 최소 비용을 출력
# 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동 가능

# 첫째 줄에 테스트 케이스의 수 T(1 <= T <= 10)
# 매 테스트 케이스의 첫째 줄 탐사 공간의 크기 N이 주어지고 N개의 줄에 걸쳐 각 칸의 비용

import heapq

T = int(input())
INF = int(1e9) 

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for i in range(T):
    
    N=int(input())
    energy=[]

    for _ in range(N):
        energy.append(list(map(int, input().split())))

    distance = [[INF]*N for _ in range(N)]
    x,y=0,0

    q=[(x, y, energy[x][y])]  
    distance[x][y] = energy[x][y]  

    while q:
        x,y,dist = heapq.heappop(q)
        if distance[x][y]<dist:             # 현재 거리가 더 작으면 스킵
            continue

        for d in range(4):                  # 인접한 좌표들
            nx = x+dx[d]
            ny = y+dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위넘어가면 스킵
                continue
            cost=dist+energy[nx][ny]
            if cost<distance[nx][ny]:  #저장된 거리값보다 코스트가 더 짧으면 변경해주고 큐에 넣기
                distance[nx][ny]=cost
                heapq.heappush(q, (nx,ny,cost))

    print(distance[N-1][N-1])



    
