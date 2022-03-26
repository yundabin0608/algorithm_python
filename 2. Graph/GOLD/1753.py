# 최단경로

# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램 구하기
# 모든 간선 가중치는 10 이하의 자연수

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# V는 정점의 개수, E는 간선의 개수, start는 시작정점 번호
V,E = map(int, input().split())
start = int(input())-1
graphs= [[] for _ in range(V)]
dp = [INF]*V
dp[start]=0

def Dijkstra(start):
    heap = []
    heapq.heappush(heap,(0, start)) ############@@@@ 왜 (start, 0)으로 바꾸게되면 시간초과가 뜨는지 궁금함
    
    while heap:
        weight, now = heapq.heappop(heap)
        # 현재 테이블과 비교해 더크면 무시
        if dp[now] < weight : 
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for nxt, w in graphs[now]:
             # 현재 정점까지 weight + 다음 정점까지 weight 이게 현재 기록된 값보다 작으면 갱신 (dp)
            nweight = w+weight
            if nweight < dp[nxt]:
                dp[nxt] = nweight
                heapq.heappush(heap,(nweight, nxt)) # 힙에삽입 
    
# u에서 v로 가는 가중치 w인 간선 존재 (u!=v, w<=10임)
for _ in range(E):
    u,v,w = map(int, input().split())
    graphs[u-1].append([v-1,w])
Dijkstra(start)
for i in dp:
    print(i if i!=INF else "INF")