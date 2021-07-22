# 전보 
# N개 도시 존재, 각 도시번호와 통로가 설치되어있는 정보 주어짐
# 각 도시는 보내고자 하는 메세지가 있다면 다른 도시로 전보를 보내서 다른 도시로 해당하는 메세지 전송
# 전보를 보내고자 한다면 그에 해당하는 방향에 맞는 통로가 있어야 한다 (간선이 방향성 존재)
# C라는 도시에서 출발해서 각 도시 사이에 설치된 통로를 거쳐 최대한 퍼져나갈것
# C에서 보낸 메세지를 받게 되는 도시 총 개수와 이 도시들이 모두 메세지 받는데 걸리는 시간?
# 범위때문에 플루이드워셜 사용 불가, 우선순위 큐 이용해서 시간복잡도 줄임

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)                              # 무한을 의미하는 값으로 10억을 설정

n, m, start = map(int, input().split())     # 노드수, 간선수, 시작 노드
graph = [[] for i in range(n + 1)]          # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n + 1)                  # 최단 거리 테이블 -> 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))                 # X번 노드 -> Y번 노드 가는 비용Z

def dijkstra(start):
   q = []
   heapq.heappush(q, (0, start))            # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
   distance[start] = 0
   while q:                                 # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)        # 최단 거리 최소인 노드 꺼내기
        if distance[now] < dist:            # 저장된 거리가 더 작다면 무시
            continue
        
        for i in graph[now]:                # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]              
            if cost < distance[i[0]]:       # 현재 노드를 거쳐 이동하는 거리가 더 짧으면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


count = 0        # 도달할 수 있는 노드 수
max_distance = 0 # 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외 => count - 1을 출력
print(count - 1, max_distance)