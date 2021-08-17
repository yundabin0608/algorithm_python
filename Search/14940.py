# 쉬운 최단거리

# 가로와 세로로만 움직일 수 있음
# 지도의 크기 n*m n: 세로, m: 가로 // 다음 n개의 줄에 m개의 숫자가 주어진다. 0: 갈 수 없는 땅, 1 :갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개
# 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

from collections import deque

n,m = map(int, input().split())
matrix=[]
move=[[-1,0],[1,0],[0,-1],[0,1]]
q=deque()

for _ in range(n):
    temp=list(map(int, input().split()))
    matrix.append(temp)

visited=[[False]*m for _ in range(n)]
answer=[[-1]*m for _ in range(n)] # 정답 거리들 모아둠

for i in range(n):
    for j in range(m):
        if matrix[i][j]==2: # 목적지부터 큐에 우선 넣고 시작    
            q.append([i,j]) 
            visited[i][j]=True
            answer[i][j]=0
        elif matrix[i][j]==0: # 못가는곳 처리   
            answer[i][j]=0
       
while q:
    x,y=map(int,q.popleft())
    for dir in range(4):
        nx=x+move[dir][0]
        ny=y+move[dir][1]
        if (0<=nx<n) and (0<=ny<m) and matrix[nx][ny]==1 and (visited[nx][ny]==False):
            visited[nx][ny]=True
            q.append([nx,ny])
            answer[nx][ny]=answer[x][y]+1

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()
