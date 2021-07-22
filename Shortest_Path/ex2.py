# 미래 도시
# 1~N번까지 회사 (노드는 회사, 도로는 간선)
# 미래 도시에서 특정 회사까지 가는 방법은 연결된 도로 이용, 간선은 양방향
# 간선 한개 이동시 1시간 소요
# A는 1번회사에서 출발, K번 회사에 들른 후, X번 회사에 갈예정, 최소시간계산 
# N의 크기가 작으므로 플로이드워셜 알고리즘 사용 가능

INF = int(1e9) 
# 노드의 개수, 간선의 개수 
n, m = map(int, input().split())  
# 2차원 리스트(그래프 표현)제작, 모든 값을 무한으로 초기화                     
graph = [[INF] * (n + 1) for _ in range(n + 1)] 

# 자기 자신->자기 자신 비용:0 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받기
for _ in range(m):
    a, b = map(int, input().split())  # A와 B가 서로에게 가는 비용은 1이라고 설정
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]


if distance >= 1e9:  # 도달 불가
    print("-1")
else:                # 도달 가능 -> 최단거리 출력
    print(distance)