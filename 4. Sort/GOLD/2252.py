# 줄 세우기

# N 명의 학생 키순으로 줄 세울것.
# 일부 학생들의 키를 비교했으며, 이 결과로 줄 세울것
# A B => A가 B 앞에 서야 함을 의미

# 위상정렬 문제 
# 차수가 0인 점을 큐에 넣고 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 지움
# 제거 후 차수가 0인 점을 또 큐에 삽입후 반복함
# 예로 4->2, 3->1 이면 2,1의 진입차수는 0 3,4 진입차수는 1 (뒷 문자가 뒤로 와야하니까)
# 우선 3,4를 큐에 넣고 3을 꺼내고 관련 간선 제거. 

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0]*(N+1)
graph =[[]for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    degree[B]+=1
    graph[A].append(B)
    queue = deque()
    answer = []

for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()
    answer.append(current)
    for tmp in graph[current]:
        degree[tmp]-=1
        if degree[tmp]==0:
            queue.append(tmp)
            
print(*answer)