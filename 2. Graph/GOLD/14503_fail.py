# 로봇청소기

# 로봇 청소기가 있는 장소 : N*M 직사각형, 1*1 정사각형들로 나뉨
# 청소기가 바라보는 방향 있으며 동,서,님,북중 하나, 각각 칸은 벽 또는 빈칸
# 지도 각 칸은 (r,c) 표현 가능 r:북으로 부터 떨어진 칸수 c: 서로부터 떨어진 칸 수
# 현위치 청소 -> 현재 방향 기준으로 왼쪽부터 차례로 인접한 칸 탐색
# 왼방향 청소X공간 있으면 그 방향으로 회전 후 다음 한칸 전진하고 청소
# 왼방향 청소 공간 없다면 그 방향으로 회전
# 네방향 모두 청소O 혹은 벽이면 바라보는 방향 우지한 채로 후진
# 4방향 모두 청소0 뒤방향도 벽이라 후진 못하면 작동 멈춤

import sys
from collections import deque
input = sys.stdin.readline

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

N,M = map(int, input().split())
r,c,d= map(int, input().split())
state=[]
result=0
for _ in range(N): # 빈칸:0 벽:1 방문시 1로 하자^^
    state.append(list(map(int, input().split())))

def bfs(x,y,d):
    queue = deque()
    global result
    result+=1
    state[y][x] = -1
    queue.append((x,y,d))
    
    while queue:
        flag = False # 상하좌우 막히고 뒤에 벽일경우 True, break 조건
        m,n,dir =queue.popleft()
        
        # 왼쪽 청소공간 있음 
        ldir = dir-1 if dir>0 else 3
        l_x, l_y = m+dx[ldir], n+dy[ldir]
        if 0<l_x<M-1 and 0<l_y<N-1 and state[l_y][l_x]==0:
             queue.append((l_x, l_y, ldir))
        # 왼쪽 청소할 공간 없음
        else:
            rdir = dir+1 if dir<3 else 0
            bdir = dir+2 if dir<2 else (0 if dir==2 else 1)
            u_x,u_y = m+dx[dir], n+dy[dir]
            r_x, r_y = m+dx[rdir], n+dy[rdir]
            b_x, b_y = m+dx[bdir], n+dy[bdir]
            
            # 상하좌우 모두 청소되었거나 벽인경우 
            if state[u_y][u_x]!=0 and state[r_y][r_x]!=0 and state[b_y][b_x]!=0:
                # 뒤가 벽아님 => 후진
                if state[b_y][b_x]!=1:
                    queue.append((b_x, b_y, dir))
                # 뒤에가 벽
                else:
                    flag=True
                    break
            else: 
                # 왼쪽으로 회전만
                queue.append((x,y,ldir) )
        
        if flag : break       
            
          
bfs(r,c,d)  
print(result)          
            
            

