# 인구이동
from collections import deque

N, L, R = map(int, input().split())
result = 0
people_num=[]

for i in range(N):
    people_num.append(list(map(int, input().split())))

move=[[-1,0],[1,0],[0,-1],[0,1]]

def bfs(x,y):
    moveq=deque()
    q.append([x,y])
    c[x][y]=1
    people=0
    count=0

    while q:
        x,y=q.popleft()
        moveq.append([x,y])
        people+=people_num[x][y]
        count+=1
        for i in range(4):
            nx=x+move[i][0]
            ny=y+move[i][1]
            if 0<=nx<N and 0<=ny<N and not c[nx][ny]:
                if L<=abs(people_num[x][y]- people_num[nx][ny])<=R:
                    c[nx][ny]=count
                    q.append([nx,ny])

    while moveq:
        x,y=moveq.popleft()
        people_num[x][y]=people//count
    
    if count==1:
        return 0
    return 1

while True:
    q=deque()
    c=[[0]*N for _ in range(N)] # c는 인구이동 구역에 들어갔는지 아닌지 체크
    count=0
    for i in range(N):
        for j in range(N):
            if not c[i][j]:
                count+=bfs(i,j)

    if not count:
        break
    
    result+=1

print(result)

# q는 인구이동??, moveq는 그때그때 인구이동할때 범위재려고 만든 큐
# 안희 q량 moveq랑 왜 밖에서 만들고 bfs 안에서 만드는지 잘 모르겠음;;;
        
# bfs로 이동하면서 인구수와 연합한 나라수 좌표를 각각 people, count, moveq에 저장
# 인구수 차이가 L~R 인 나라를 방문할 수 있을때까지 방문
# moveq에서 좌표를 하나씩 불러와 총 인구수를 총 나라로 나눈값으로 바꿈
# 연합한 나라수가 없으면 0 아니면 1반환 => 연합했는지 체크 (종료조건) bfs return 값 합이 0
# 위 과정을 방문하지 않은 나라에 대해 bfs로 모두 검사

