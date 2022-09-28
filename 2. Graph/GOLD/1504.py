# 특정한 최단 경로

# 방향성이 없는 그래프, 세준이는 1>N으로 최단 거리로 이동할 것. 
# 단, 임의로 주어진 두 정점을 통과하면서 이동하는 특정한 최단 경로를 구할것
# 한번 이동했던 정점 및 간선 재이동 가능, 최단거리만 보장하면 됨


import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N,E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,dist = map(int, input().split())
    graph[a].append((dist, b))
    graph[b].append((dist, a))
V1, V2 = map(int,input().split())

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0

    while hq:
        dist, node = heapq.heappop(hq)

        if distance[node] < dist: continue

        for next_dist, next in graph[node]:
            tmp = next_dist + dist
            if distance[next] > tmp:
                distance[next] = tmp
                heapq.heappush(hq, (tmp, next))

    return distance

# 1>v1>v2>N : 1>v1 v1>v2 v2>N
# 1>v2>v1>N : 1>v2 v2>v1 v1>N 두가지의 경우 비교 무한대일 경우 -1 출력
start, v1, v2 = dijkstra(1), dijkstra(V1), dijkstra(V2)
answer = min(start[V1]+v1[V2]+v2[N], start[V2]+v2[V1]+v1[N])
print(answer if answer<INF else -1)
