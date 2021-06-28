#특정 거리의 도시찾기

from collections import deque
#import sys
#input = sys.stdin.readline 이거 해줘야 시간안에 제출됨

N,M,K,X=map(int,input().split(' '))

# 도시간의 인접리스트 작성
path = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    path[a].append(b)

# 도시의 최단거리 리스트 생성                
distance=[-1]*(N+1) # 구간을 0~ 말고 1부터할라고 N+1 한건강
distance[X]=0
 

queue=deque([X])
while queue:
    now=queue.popleft()
    for next in path[now]:
        if distance[next] == -1:
            # 최단거리 갱신 (-1이면 안방문한거니까) ***** 여기가 키 포인트 *****
            queue.append(next)
            distance[next]=distance[now]+1

# 최단거리 k인 도시들 오름차순 출력
check=False
for i in range(N+1):
    if distance[i]==K:
        print(i)
        check=True
# 최단거리 도시 존재X
if check == False:
    print(-1)