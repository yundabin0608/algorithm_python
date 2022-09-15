# 트리와 쿼리

# 간선에 가중치, 방향성 없는 루트 있는 트리 있을때 정점 U를 루트로 하는 서브트리의 정점의 수 출력
# bfs는 시간초과
import sys
input = sys.stdin.readline
from collections import deque

N,R,Q = map(int, input().split())
tree = [[] for _ in range(N+1)] 
for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
qs = [int(input()) for _ in range(Q)]

# 입력 기반으로 루트 -> 그 밑의 자식만 남기도록 할 것
q = deque()
q.append([R,0])
while q:
    node, parent = q.popleft()
    # 부모 있다면 트리에서 제거 (밑의 자식만 남길 것)
    if parent!= 0 : tree[node].remove(parent)
    for next in tree[node]: q.append([next,node])
            
# 해당 쿼리를 루트로 하는 서브트리의 정점 수 출력
for q in qs:
    queue = deque()
    queue.append(q)
    count = 0
    while queue:
        tmp = queue.popleft()
        count += 1
        for nxt in tree[tmp]:
            queue.append(nxt)
    print(count)

# 55퍼센트까지 성공 그뒤 시간초과
# 형식 노드는 N개, 간선은 N-1개임 무조건
# 1 : 3
# 2 : 3
# 3 : 1 4 2
# 4 : 3 5
# 5 : 4 6
# 6 : 5 7 9 8
# 7 : 6
# 8 : 6
# 9 : 6

# 5: 4 6 / 2
# 4: 3 / 1
# 6: 7 9 8 / 3
# 3: 1 2 / 2
# 1 2 7 8 9 없음 / 0

# node, parent = q.popleft()
#     for next in tree[node]:
#         # 부모 있다면 트리에서 제거 (밑의 자식만 남길 것)
#         if next == parent : 
#             tree[node].remove(next)
#         else : 
#             q.append([next,node])
#             print("next")
#     print(*q)
# 이런 코드는 tree[node]가 하나 삭제되므로 뒤에꺼 한개씩 밀리게 됨

