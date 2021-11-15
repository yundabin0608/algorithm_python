# 토마토

# 익은 토마토들 근처(위,아래,왼,오,앞,뒤)에 익지 않은 토마토를 두고 하루가 지나면 익음 
# 입력 - M(가로),N(세로),H(높이) (M,N -> 2~100, H -> 1~100), 1:익은토맛 0:안익은토맛 -1:없음
# 토마토가 모두 익을때까지 몇일 걸리는지 모두 못익으면 -1 출력

# bfs 이용
from collections import deque
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

queue=deque()
def bfs():  # 토마토를 한칸씩 점점 익혀나가는것. 토마토에 익혀질때마다 그전숫자+1 해서 적어놓기
    while queue:
        x,y,z=queue.popleft()
        visit[z][x][y]=1
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny]==0 and visit[nz][nx][ny]==0:
                queue.append([nx,ny,nz])
                tomato[nz][nx][ny]=tomato[z][x][y]+1 
                visit[nz][nx][ny]==1
            
    

M,N,H = map(int,input().split())
tomato=[]
visit=[[[0 for i in range(M)] for j in range(N)] for k in range(H)]
answer=0
flag=False

for i in range(H):
    tomato.append([])
    for _ in range(N):
        tomato[i].append(list(map(int, input().split())))
for c in range(H):
    for a in range(N):
        for b in range(M):
            if tomato[c][a][b]==1:
                queue.append([a,b,c])
bfs()
for c in range(H):
    for a in range(N):
        for b in range(M):
            if tomato[c][a][b]==0: # 토마토 전부 익은게 아니라면 flag 바꿔주기
                flag=True
            answer=max(answer, tomato[c][a][b]) # 익을때마다 +1씩 해주니까 정답은 answer-1

if flag: print(-1)
else: print(answer-1)