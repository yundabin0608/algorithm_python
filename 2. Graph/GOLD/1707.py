# 이분 그래프

# 정의
# 그래프의 정점의 집합을 둘로 분할, 각 집합에 속한 정점끼리는 서로 인접하지 않게 분할가능
# 그래프가 입력으로 주어졌을때 이분그래프인지 아닌지 판별, 그래프는 무방향

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node, team):
    visited[node] = team
    for i in matrix[node]:
        # 안가봤으면 방문
        if visited[i]==0 :
            if not dfs(i,-team): 
                return False
        # 가봤고 같은 그룹이면 F
        elif visited[i]==visited[node]:
            return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    matrix = [[] for _ in range(V)]
    visited = [0]*V
    for _ in range(E):
        i,j = map(int, input().split())
        matrix[i-1].append(j-1)
        matrix[j-1].append(i-1)
    
    for v in range(V):
        if visited[v]==0:
            flag = dfs(v,1)
            if not flag:
                break

    if flag: print("YES")
    else : print("NO")