# 줄 세우기

# N 명의 학생 키순으로 줄 세울것.
# 일부 학생들의 키를 비교했으며, 이 결과로 줄 세울것
# A B => A가 B 앞에 서야 함을 의미

# 위상정렬 문제 
# 차수가 0인 점을 큐에 넣고 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 지움
# 제거 후 차수가 0인 점을 또 큐에 삽입후 반복함
# 예로 4->2, 3->1 이면 2,1의 진입차수는 0 3,4 진입차수는 1 (뒷 문자가 뒤로 와야하니까)
# 우선 3,4를 큐에 넣고 3을 꺼내고 관련 간선 제거. 
# 위상정렬은 방향그래프로, 그래프 내의 정점들을 순서에 맞게 정렬하며, 간선의 방향이 순서를 나타냄
# 진입차수와 진출차수가 있으며, 진입차수는 밖에서 한 정점으로 들어오는 간선수, 진출차수는 정점에서 나가는 간선수

# 위상정렬은 진입차수가 0인 정점과 이와 관련된 간선을 모두 지우고 정점의 진입차수를 갱신하는것을 반복

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0]*(N+1)
graph =[[]for _ in range(N+1)]
queue = deque()
answer = []

# 진입 차수 업데이트하면서 방향그래프 표현
for _ in range(M):
    A,B = map(int,input().split())
    degree[B]+=1
    graph[A].append(B)

# 진입 차수 0인것들 모아서 큐에 넣기
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

# 큐에 있는 값 빼고 그와 관련된 정점의 진입차수 빼주기, 진입차수 0이면 큐에 또 넣어주기
while queue:
    current = queue.popleft()
    answer.append(current)
    for tmp in graph[current]:
        degree[tmp]-=1
        if degree[tmp]==0:
            queue.append(tmp)    
print(*answer)