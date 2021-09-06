# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1으로 나뉘며 한 칸에는 물고기 최대 1마리.
# 아기 상어와 물고기는 모두 크기를 가지며 맨처음 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 즉 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

# 첫줄: 공간의 크기N, 둘째줄: 공간 상태 0-빈칸 1~6-물고기크기 9-아기상어위치
# 물고기 잡아먹을수 있는 시간 출력

from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

N=int(input())
matrix=[]

def bfs(i, j):
    visit = [[0] * N for i in range(N)] # 방문기록에 관한것
    visit[i][j] = 1
    eat = []
    dist = [[0] * N for i in range(N)]
    
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny= x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0: # 방문한적 없고 matrix안에 있으면
                # 아기상어보다 작거나 같은 물고기 혹은 없는경우 큐에 넣고 방문처리 => 지나갈 수 있으므로
                if matrix[nx][ny] <=  matrix[i][j] or matrix[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                # 아기상어보다 작은물고기의 경우 eat배열에 넣기
                if matrix[nx][ny] < matrix[i][j] and matrix[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat: # 먹을물고기 없으면 음수 반환
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1])) # 물고기 먹는 기준이 있으므로 정렬후 리턴
    return eat[0][0], eat[0][1], eat[0][2]

for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(N):
        if matrix[i][j]==9:
            matrix[i][j]=2
            bShark=[i,j]

exp = 0
cnt = 0
while True:
    i, j = bShark[0], bShark[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1: break

    [ex][ey] = matrix[i][j]
    matrix[i][j] = 0 # 물고기 먹으니까 0
    bShark = [ex, ey] # 아기상어 위치
    exp += 1         # 아기상어 크기 증가시킴
    if exp == matrix[ex][ey]:
        exp = 0
        matrix[ex][ey] += 1
    cnt += dist # 이동시간(=거리)증가
print(cnt)   
