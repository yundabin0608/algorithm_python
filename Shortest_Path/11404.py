# 플로이드
# n(2 ≤ n ≤ 100)개 도시 , 도시->다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스 
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하기

# 첫째 줄 : 도시개수 n 둘째 줄 : 버스의 개수 m 셋째 줄 ~ m+2줄 : 버스의 정보 (시작 도시 a, 도착 도시 b, 필요비용 c)
# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
# n개의 줄을 출력, i번째 줄에 출력하는 j번째 숫자는 도시 i->j로 필요한 최소 비용 못간다면 0

# 모든 도시쌍에 대해 출력해야하므로 플로이드워셜을 이용

INF = int(1e9) 
n = int(input()) 
m = int(input())
                   
graph = [[INF] * (n + 1) for _ in range(n + 1)] 

for _ in range(m):
    a, b, c = map(int, input().split()) 
    if graph[a][b]>c:
        graph[a][b]=c

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()