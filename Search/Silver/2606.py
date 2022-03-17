# 바이러스

# 어느날 1번 컴퓨터가 바이러스 걸렸을때, 1번 컴퓨터를 통해 바이러스 걸리는 컴터수

N = int(input())  # N<=100
pair = int(input())
pairs = [[0]*N for _ in range(N)]
result = [0 for _ in range(N)]

def dfs(v):  # 해당 노드 방문했다고 표시
    result[v] = 1
    for i in range(N): # 해당 노드의 연결된 컴퓨터들이면서 결과에 없으면 
        if pairs[v][i]==1 and result[i]==0:
            dfs(i)


for _ in range(pair):   
    a, b = map(int, input().split())
    pairs[a-1][b-1] = 1
    pairs[b-1][a-1]=1
    
dfs(0)
r=0
for j in range(1,N): # (0,0)제거
    if result[j]==1:
        r+=1
print(r)
        

    
