# 연구소 
from itertools import combinations
from collections import deque
import copy


# 바이러스가 퍼질수 있는 만큼 퍼지도록 하는 함수
def bfs(tmp):
    q=deque([])
    visited=[[False]*M for _ in range(N)]
    global result

    for virus in virus_index:
        q.append(virus)

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny= x+move[i][0], y+move[i][1]
            if 0<=nx<M and 0<=ny<N:
                if tmp[nx][ny]==0 and visited[nx][ny]==False:
                    q.append([nx,ny])
                    tmp[nx][ny]=2
                    visited[ny][nx]==True

                    

move=[[-1,0],[1,0],[0,-1],[0,1]]
matrix=[]
virus_index=[] # virus는 바이러스 퍼뜨릴때 큐에다 바이러스 있는 좌표 넣으려고 담아둠
empty_index=[] # empty는 벽을 임의로 세울 combination 결정할때 씀
result=0

N, M= map(int, input().split())

for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(M):
        if matrix[i][j]==0:
            empty_index.append([i,j])
        if matrix[i][j]==2:
            virus_index.append([i,j])


# 빈칸중에 3개 무작위로 벽세우기 => 바이러스 퍼지게 한 후 안전영역크기 세어주기
for wall in combinations(empty_index,3):
    temp = copy.deepcopy(matrix)  # 매번 기존 맵에다가 벽을 새로 세워야 하니까
    for x,y in wall:
        temp[x][y]=1

    # 벽 세웠고 바이러스 퍼뜨리기
    bfs(temp)

    count=0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                count+=1

    if count>result:
        result=count


print(result)

# 2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy 메서드 대신 
# copy 모듈의 deepcopy 함수를 사용해야 합니다 copy.deepcopy()
