# 파티

# N개 숫자로 구분된 마을에 각 한명씩 학생 거주
# N명의 학생이 X번 마을에 모여 파티, 마을 사이 M개 단방향도로가 있으며 각각 T시간 소비
# N명의 학생중 오고가는데 가장 많은 시간이 걸린 학생의 시간 출력

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int, input().split())
road = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, time = map(int, input().split())
    road[a].append((time, b))

# start 기준 다른 노드로 가는데 소요되는 시간 리스트 리턴
def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    times = [INF] * (N + 1)
    times[start] = 0

    while hq:
        t, node = heapq.heappop(hq)

        if times[node] < t: continue

        for tmp_time, tmp_node in road[node]:
            tmp = t + tmp_time
            if times[tmp_node] > tmp:
                times[tmp_node] = tmp
                heapq.heappush(hq, (tmp, tmp_node))

    return times


result = 0
backX = dijkstra(X)
for i in range(1, N + 1):
    goX = dijkstra(i)
    result = max(result, goX[X] + backX[i])
    # i>X>i 로 돌아가야 하고 길은 단방향이므로 X기준 다익스트라를 하나 더 두어서 왕복을 구한다

print(result)