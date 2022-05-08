# 중량제한

# N (2~10,000)개 섬으로 이뤄진 나라. 몇개 섬사이엔 다리 설치
# 두 섬에 공장을 세워두고 공장들이 서로 물품을 옮김 단, 중량제한 존재
# 한 번의 이동에서 옮길 수 있는 물품들의 중량 최대 값 구하기
# bridge A<->B 다리 최대중량 C. 다리는 양방향. N개섬, M개 다리

import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int, input().split())
bridge = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int, input().split())
    bridge[A].append([B,C])
    bridge[B].append([A,C])
start, end = map(int, input().split())

# mid 무게로 다리를 건널 수 있는지 판단 check가 0이면 안지나감, 1이면 지나감
def bfs(mid):
    q = deque()
    q.append(start)
    check = [0]*(N+1)
    check[start] = 1

    while q:
        x = q.popleft()
        for b,c in bridge[x]:
            if check[b]==0 and c >= mid:
                check[b]=1 
                q.append(b)

    return True if check[end]==1 else False

result, front, back = 0, 1, 1000000000 #front, back은 c의 범위
while front<=back:
    mid = (front+back)//2
    if bfs(mid): result, front = mid, mid+1
    else : back = mid - 1

print(result)