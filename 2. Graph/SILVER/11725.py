# 트리의 부모 찾기

# 루트 없는 트리가 주어질때, 루트를 1이라고 하면 각 노드의 부모 구할것
# 입력으로는 노드의 개수와 그 이후 줄에서는 노드와 연결된 두 정점이 주어짐
# 결과 : 2번노드부터 순서대로 출력
# bfs 이용해도 괜찮을듯 (stack과 visited 배열 이용해서)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
result = [0]*(N+1) 
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b) 
    tree[b].append(a)

def dfs(node):

    for t in tree[node]:
        
        # 부모가 아닐 경우
        if t != result[node]: 
            result[t] = node
            dfs(t)
       
dfs(1)
print(*result[2:])



# 1: 2 3
# 2: 1 4
# 3: 1 5 6
# 4: 2 7 8
# 5: 3 9 10
# 6: 3 11
# 7: 4
# 8: 4
# 9: 5
# 10: 5
# 11: 6
# 12: 6