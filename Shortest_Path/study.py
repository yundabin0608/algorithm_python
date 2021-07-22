# 동작과정
# 출발노드 설정 => 최단거리 테이블 초기화 (무한으로 설정, 자기자신은 0)
# 이후 반복 ( 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 => 해당 노드를 거쳐 다른 노드로 가는 비용 계산해서 최단 거리 테이블 갱신)

# 다익스트라 알고리즘의 특징
# 그리디알고리즘에 속함 : 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 이 과정 반복
# 단계를 거치며 한번 처리된 노드의 최단 거리는 고정되어 더이상 변화하지 않음 = 한단계당 하나의 노드에 대한 최단거리 찾기
# 다익스트라 알고리즘을 수행한 뒤엔 테이블에 각 노드까지의 최단 거리 정보가 저장됨
# 구현법 : 매 단계마다 방문하지 않은 노드중 최단 거리가 가장 짧은 노드를 택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차탐색)


import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기  (연결리스트의 형태로 저장)
graph = [[] for i in range(n + 1)]
# 방문 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 매번 단계 반복시 사용됨
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 출발 노드 방문처리
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]  # 현재 선택된 노드까지 거리 + 현재 노드에 연결된 거리값 
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


#============================================================================================
# 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 예) 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내는 경우
# 표준 라이브러리 형태로 지원 : 스택/ 큐/ 우선순위 (별도의 우선순위 설정)
# 우선순위 큐 구현을 위해 힙(Heap) 사용
# 최대힙 (미지원,=> 최소힙에 -value로 넣음)과 최소힙 (지원)
# 큐에 데이터를 넣을때 튜플형태로 묶어서 넣고 (거리: , 노드: ) 이런식으로 넣으면 편리
# 우선순위 큐에서 꺼낸 거리의 값이 기록된 값보다 크면 무시

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 별도의 방문처리 확인을 위한 테이블이 필요하지 않음
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 매번 현재 상황에서 가장 최단거리가 짧은 노드를 택하기 위한 함수가 필요없음
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 우선순위큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q) # 힙으로 시간복잡도 보장
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드까지의 거리값 + 인접한 노드까지 거리값
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

#============================================================================================
# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
# 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘 수행
# but 매 단걔마다 방문하지 않는 노드 중에서 최단 거리를 갖는 노드를 찾는 과정 필요하지 않음
# 2차원 테이블에 최단 거리 정보를 저장하며 다이나믹 프로그래밍 유형에 속함 (행: 출발노드, 열: 도착노드)
# 노드의 개수가 매우 적은 경우에 사용 가능 

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화 (각각이 1번부터 출발한다고 생각하므로)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행 (k: 거쳐가는 노드, a: 출발노드, b: 도착노드)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()