# 트리

# 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.
# 트리의 성질
# 트리는 사이클 X 정점이 n개, 간선이 n-1개. 임의의 두 정점에 대해서 경로가 유일하다.
# 그래프가 주어졌을 때, 트리의 개수를 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

# 노드들로 구성된 트리가 여러 개 있을 수 있으므로 방문여부 파악하면서 셀 것
# 예로 1-2-3-4-5 6-7-8 9-10 이런식일 수 있으므로 1,6,9 확인 해야하니깐
# 방문 안했을때, 자식이 있다면 재귀호출, 사이클 있다면 False
# def find_tree(node, parent):
#     # dfs 사용
#     visited[node] = True
#     for tmp in tree[node]:
#         if tmp != parent:
#             if visited[tmp]: return False
#             flag = find_tree(tmp, node)
#             if not flag : return False
#     return True
#+++=====+=========> 이거 고쳐보기

def find_tree(node):
    flag = True
    q = deque()
    q.append(node)
    while q:
        tmp = q.popleft()
        # bfs 이므로 return으로 끝내버리면 안되고 전부 다 돌아서 False 없을때 트리
        if visited[tmp] : 
            flag = False
        visited[tmp] = True
        for next in tree[tmp]:
            if not visited[next]:
                q.append(next)
    return flag

case = 0
while(True):
    case+=1
    n, m = map(int, input().split())
    if n==0 and m==0 : break

    tree = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        if a==b: continue
        tree[a].append(b)
        tree[b].append(a)

    T = 0
    for i in range(1,n+1):
        if not visited[i]:
            if find_tree(i): T+=1

    if T == 0 : print("Case %d: No trees." %case)
    elif T==1 : print("Case %d: There is one tree." %case)
    else : print("Case %d: A forest of %d trees." %(case, T))