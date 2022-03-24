# 보물섬
# 자꾸 채점하다가 60프로에 시간초과가 뜨게 됨 해결 못해서 pypy3로 수행

# 보물섬 지도는 직사각형 모양으로 육지(L), 바다(W)로 나뉘며 이동은 상하좌우로만 가능
# 한칸 이동시 한시간이 걸리며, 보물은 서로간 최단거리로 이동하는데 있어 가장 긴 시간 걸리는 육지 두곳에 나뉘어 있음
# 육지사이 이동시 같은곳 두번이상 가거나 멀리 돌아가면 안됨
# dfs로 A->B육지를 간다고 했을때 도착거리가 최단이라고 보장할 수 없거나 너무 많은 경로를 봐야 할거 같아서 dfs 이용
import sys
from collections import deque
input=sys.stdin.readline

n,m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,cnt):
    visited = [[0]*m for _ in range(n)]
    count = 0
    queue = deque()
    queue.append((x,y,cnt))
    visited[y][x]=1
    while queue:
        tx, ty, tcnt = queue.popleft()
        if count < tcnt: count=tcnt  # count를 최대값으로 유지
        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx]=='L' and visited[ny][nx]==0:
                # nx, ny 가 범위내에 존재하고 육지이며 방문한 적 없을경우
                # 방문표시 후 현좌표 cnt에 다음좌표로 갈땐 cnt+1로 1 더함
                visited[ny][nx]=1
                queue.append((nx,ny,tcnt+1))
    return count  

# n 세로 m 가로
for _ in range(n):
    # 리스트 생성시 '\n' 제거를 위해 rstrip() 함수 이용
    graph.append(list(input().rstrip())) 
    
result=0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'L':
            result=max(result, bfs(x,y,0)) 
            # 각각의 자리에서 실행했던 결과들 중 최댓값으로 매번 갱신
print(result)