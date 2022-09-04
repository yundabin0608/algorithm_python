# 경로 찾기

# 가중치 없는 방향 그래프 G
# 모든 정점 (i,j) 에 대해 i -> j 인 경로가 있는지 없는지 구할 것
# 1의 경우 간선 있음, 0의 경우 없음

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = []

for node in range(N):
    tmp = [0]*N
    visited = [False]*N
    start = []
    for i in range(N):
        if matrix[node][i]==1: 
            start.append(i)
            visited[i] = True
    q = deque(start)
    while q:
        n = q.popleft()
        tmp[n] = 1
        for i in range(N):
            if matrix[n][i]==1 and visited[i]==False:
                q.append(i)
                visited[i]=True
    answer.append(tmp)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=" ")
    print()




