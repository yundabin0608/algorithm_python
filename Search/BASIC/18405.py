# 경쟁적전염
from collections import deque

N,K=map(int,input().split())

matrix=[]
virus=[]

for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(N):
        if matrix[i][j]!=0:
            virus.append([matrix[i][j],i,j,0])
# matrix를 읽어가며 바이러스가 있는 부분은 바이러스 리스트에 (숫자(바이러스종류),x,y(바이러스좌표),시간) 입력

S,X,Y=map(int, input().split())

#좌,우,하,상 방향
move = [[-1,0],[1,0],[0,-1],[0,1]]

# 낮은 종류의 바이러스부터 증식하므로
virus.sort()
queue=deque(virus) # 바이러스의 좌표 들어있는 리스트를 큐에 넣는다

while queue:
    virus, x, y, time = queue.popleft()
    if time==S:
        break
    for i in range(4): #상하좌우
        dx=x+move[i][0]
        dy=y+move[i][1]
        if dx>=0 and dx<N and dy>=0 and dy<N:
            if matrix[dx][dy]==0:
                matrix[dx][dy]= virus
                queue.append((virus, dx, dy, time+1))

# 리스트여서 0부터시작하므로 조작
X-=1
Y-=1
print(matrix[X][Y])

