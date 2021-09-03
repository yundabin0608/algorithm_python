# 그대, 그머가 되어

# 머호는 a를 b로 바꾸려고 하고 n개의 문자와 치환가능한 문자쌍 m개가 주어짐
# 입력 - 1: 머호가 바꾸려는 문자 a,b 2: 전체 문자의 수N과 치환가능한 문자쌍 수 M (1<=N<=1000, 1<=M<=10000) 이후 m개 줄에 걸쳐 문자쌍 주어짐
# 출력 a를 b로 바꾸기 위해 필요한 최소 치환 횟수 출력. 불가능시 -1 출력, 모든 문자는 N이하 자연수로 표현
# 다익스트라로 풀것인데, 문자를 c->d 이든 d->c이든 상관없으므로 양방향, 간선비용을 모두 1이라고 생각할것
import heapq
import sys
INF = int(1e9)

a,b=map(int, input().split())
n,m=map(int, input().split())

graph =[[]for i in range(n + 1)]
distance = [INF]*(n+1)

for _ in range(m):
    # x->y 또는 y->x 로 가는 비용이 1
    x,y=map(int, input().split()) 
    graph[x].append(y)
    graph[y].append(x)

def dijkstra(start, end):
    q = []
    # 시작하는곳으로 가는 최단 경로 0
    heapq.heappush(q, (0, start))
    distance[start]=0 

    # 시작과 끝이 같은 경우는 제외
    if start == end: 
        return 0
    
    # 큐가 비어있지 않다면
    while q:  
        dist, now = heapq.heappop(q) # 거리(치환수), 현재 문자

        if distance[now] < dist:  continue  # 현재의 치환한 수가 더 크다면 그냥 넘어감
        for i in graph[now]:                # 현재 알파벳에서 바꿀수 있는 알파벳들 = i
            cost = dist + 1                 # 치환할때 +1씩 되므로 cost=dist+1
            # 치환하려는 알파벳의 distance가 cost보다 크다면 치환수를 cost로 바꾸고 큐에 넣기
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
            # 도착점에 다다르면 cost를 아니면 -1을 리턴
            if i == end: 
                return cost
    return -1

print(dijkstra(a, b))