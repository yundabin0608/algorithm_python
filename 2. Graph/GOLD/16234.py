# 인구이동

# N*N 땅, 1*1에 1나라, 그나라엔 A[r][c] 명 존재, 국경선은 정사각형
# 인구이동은 하루진행 
# 국경선 공유하는 두나라 L<=인구차<=R 일때 국경선 열림
# 각각의 국경선들이 모두 열렸다면 인구이동 시작, 국경선 열려서 이어진나라들이 연합. 이사이에서 이동
# 각 연합을 이루는 각 칸 인구수는 연합인구수/연합이루는 칸 개수. 소수점 버림
# 연합 해체후 국경선 닫기
# 인구이동 몇일 발생할까

import sys
import math
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N,L,R = map(int, input().split())
popular = []
for _ in range(N):
    popular.append(list(map(int, input().split())))
visited = [[-1]*N for _ in range(N)]
union = deque([i,j] for i in range(N) for j in range(i%2,N,2))
count = 0

while 1 :
    queue = deque()
    for _ in range(len(union)):
        i,j = union.popleft()
        if visited[j][i] == count: continue
        visited[j][i] = count
        lands = set([(i,j)])
        people= popular[j][i]
        queue.append((i,j))
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<N and 0<=ny<N and visited[ny][nx]!=count:
                    if L<=abs(popular[ny][nx]-popular[y][x])<=R:
                        visited[ny][nx]=count
                        lands.add((nx,ny))
                        people+=popular[ny][nx]
                        queue.append((nx,ny))
        if len(lands)>1:
            avg = people//len(lands)
            for x,y in lands:
                popular[y][x] = avg
                union.append((x,y))
                
    if union:
        count+=1
    else:
        break
print(count)
                        