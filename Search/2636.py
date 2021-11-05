# 치즈

# N*M 판에 1:치즈, 0: 치즈없음 (N: 1~100)
# 0: 공기와 닿은 부분은 한시간 후에 녹으며 치즈안의 구멍은 안녹음
# 몇시간 후에 치즈가 다 녹을지 답하기

# 보자마자 search 라고 생각. 치즈의 테두리 따는게 중요하겠다고 생각 (=>구멍판별)
# 0에서 상하좌우 둘러볼때 1이면 무조건 가장자리. 구멍일 수 없음

import sys
from collections import deque

N,M=int(input().split())
cheese=[]
for i in range(N):
    cheese.append(list(map(int, input().split())))
    

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count=0
answer=0
while True:
    border=[]
    q=[(0,0)]
    # 지나간곳은 모두 -1로 바뀌고 치즈 없는곳은 q, 치즈 테두리는 border의 큐로 넣기
    while q:
        y,x=q.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if cheese[ny][nx]==0:
            cheese[ny][nx]=-1
            q.append((ny,nx))
        if cheese[ny][nx]==1:
            cheese[ny][nx]=-1
    
    if not border: break

    answer+=1
   
