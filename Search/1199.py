# 오일러 회로

# 입력 - 첫 줄 : 정점의 수 N(1 ≤ N ≤ 1,000) 
# i+1번째 줄에는 i번 정점에 대한 인접행렬이 주어진다. 두 정점 사이에 간선이 여러 개 O 
# 인접행렬의 값 = 두 정점 사이의 간선 개수 (0~10 사이)
# 입력으로 주어지는 그래프에는 루프 (양 끝점이 같은 간선)는 없다. 또, 입력으로 주어지는 그래프는 모두 연결되어 있다.

# 출력 - 첫 줄에 방문하는 점 순서를 공백으로 구분하여 출력한다. (단, 시작점은 어느 위치에서든 상관없고 아무 경로만 하나 찍으면 된다. 불가능한 경우에는 -1을 출력한다.)


# DFS로 search, 한번간 곳은 다시 못가므로 표시, 양방향그래프는 방향성 없다고 보면됨 그냥 선으로 표현
# 오일러 경로를 만족했을때(모든 간선을 지나는데 한번 지난 간선은 다시 가지 않음) 경로 출력할것. 오일러경로는 한붓그리기 같은것

#오일러 회로 구하는 방법
# 1. 임의의 정점 V를 잡고 dfs를 돌려서 V로 다시 돌아오는 사이클 => 그 경로를 P
# 2. 그래프의 모든 정점을 탐색하지 않았다면, P에서 탐색하지 않은 간선이 있는 정점 V’를 찾아 해당 정점부터 dfs를 다시 돌림 => 그 경로를 P’
# 3. P와 P’를 합칩니다.
# 4. 그래프 상에 있는 모든 정점을 탐색할 때까지 2, 3번을 반복

import sys
sys.setrecursionlimit(10**9)

N=int(input())
matrix=[]

for _ in range(N):
    matrix.append(list(map(int, input().split())))


def dfs(now):
    for i in graph[now]:
        if matrix[now][i]:
            matrix[now][i]-=1
            matrix[i][now]-=1
            dfs(i)
    print(now+1,end=" ")


graph={}
for i in range(N):
    graph[i]=[]
    rowSum=0
    for j in range(N):
        for _ in range(matrix[i][j]):
            rowSum+=1
            graph[i].append(j)
    # 두 정점을 연결하는 간선의 수가 짝수여야만 오일러 회로 존재
    if rowSum%2==1: 
        print(-1)
        sys.exit()

dfs(0)