import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,R,Q = map(int, input().split())
tree = [[] for _ in range(N+1)] 
for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
qs = [int(input()) for _ in range(Q)]

# 노드 내려가면서 그 밑의 것들 모두 덧셈해 기록
def dfs(node):
    answer[node]=1
    for i in tree[node]:
        if answer[i] == 0: 
            dfs(i)
            answer[node]+=answer[i]

answer = [0]*(N+1)
dfs(R)

for q in qs:
    print(answer[q])