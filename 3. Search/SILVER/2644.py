# 촌수계산

# 부모-자식 : 1촌, 이로부터 사람간 촌수 계산

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p1, p2 = map(int, input().split())
relation = [[] for _ in range(n+1)]
check = [0]*(n+1) # 방문겸 몇촌인지 기록

def dfs(p):
    for tmp in relation[p]:
        if check[tmp]==0:
            check[tmp]= check[p]+1
            dfs(tmp)

for i in range(int(input())):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

dfs(p1)
print(check[p2] if check[p2]>0 else -1)