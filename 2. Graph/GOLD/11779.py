# 최소비용구하기 2

# n(1~1000)개 도시와 m(1~100000)개 버스
# A->B 로 가는데 드는 버스 최소비용과 경로 출력

import sys, heapq, copy
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)] 
path = [[] for _ in range(n + 1)] 

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(start):
    distance = [INF for _ in range(n+1)] # 최소비용관련 리스트, 시작 지점은 0
    distance[start] = 0 
    q = []
    heapq.heappush(q, (0, start)) 

    while q:
        cost, way = heapq.heappop(q)

        if distance[way] < cost:
            continue

        # 최단 거리가 갱신되는 경우라면 
        # - 자신 -> 다른 곳인 경로와 길이가 수정되었을 것이므로 바꾸기 (현재까지의 경로+자기자신)
        path[way].append(way)

        if way == end: return distance[end]

        # end와 일치하지 않는다면 최단 거리 수정
        for new_cost, new_way in graph[way]:
            # 현재 노드를 거쳐가는게 더 최소비용이면 갱신
            if distance[new_way] > new_cost + cost:
                distance[new_way] = new_cost + cost
                heapq.heappush(q, (distance[new_way], new_way))              
                path[new_way] = copy.deepcopy(path[way]) # 최단 거리 수정으로 인해 최단 경로 수정, 따로 만들어서 참조하지 못하도록 할 것       

print(dijkstra(start))
print(len(path[end])) 
print(*path[end]) 