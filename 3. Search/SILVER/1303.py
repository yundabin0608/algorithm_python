# 전쟁 - 전투 

import sys
input = sys.stdin.readline
from collections import deque

N,M =map(int,input().split())
soldier = [input() for _ in range(M)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

visited = [[True]*N for _ in range(M)]
answer1, answer2 = 0,0

def bfs(a,b,color):
    
    q = deque()
    q.append([a,b])
    visited[b][a] = False
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[ny][nx]==True and soldier[ny][nx]==color:
                    count+=1
                    visited[ny][nx]=False
                    q.append([nx,ny])

    return count**2

for m in range(M):
    for n in range(N):
        if visited[m][n] == True:
            if soldier[m][n]=="W":
                answer1 += bfs(n,m,"W")
            else:
                answer2 += bfs(n,m,"B")

print(answer1, answer2)