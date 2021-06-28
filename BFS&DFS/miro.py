from collections import deque

n,m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int.split())))

#이동할 네 방향 정의 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,-]

#BFS 구현코드
def bfs(x,y):
    #큐 구현위한 라이브러리 사용
    queue=deque()
    queue.append(x,y)

    while queue:         #큐가 빌때까지 반복
        x,y=queue.popleft()
        #현 위치에서 4방향 위치확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue  #미로 찾기 공간 아니면 무시
            if graph[nx][ny]==0:
                continue  #벽이면 무시
            #해당노드 첫방문의 경우에만!! 최단거리기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

    print(bfs(0,0))