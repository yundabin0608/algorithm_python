# 욕심쟁이 판다

# n × n의 크기의 대나무 숲, 상하좌우로 움직임 가능 단 전 지역보다 대나무가 많을경우만 이동

# 입력 - 1: 대나무 숲의 크기 n(1 ≤ n ≤ 500) 2~n+1: 대나무 숲의 정보(대나무의 양); 1,000,000보다 작거나 같은 자연수
# 출력 - 판다가 이동할 수 있는 칸의 수의 최댓값

# => 메모제이션과 dfs를 이용하도록 할것

import sys
sys.setrecursionlimit(1000000) #dfs 깊이때문에 달아줘야함

n=int(input())
tree=[]  # 대나무숲 정보 입력
dp=[]    # 각 칸당 몇번 움직였는지 기록할것임

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    tree.append(list(map(int, input().split())))
    dp.append([0]*n)

def dfs(x,y):
    if dp[x][y]>0: # 몇번 움직였는지에 대한 정보가 없을 경우에만 수행 있으면 그 값 이용
        return dp[x][y]

    dp[x][y]=1 # 일단 그 자리 = 1칸
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if (0<=nx<n and 0<=ny<n and tree[x][y]<tree[nx][ny]):
            # 상하좌우 움직이면서 이중 가장 큰 값 사용할것이고 여기서 재귀적으로 또 호출
            dp[x][y]=max(dp[x][y], dfs(nx,ny)+1)
    
    return dp[x][y]
    
count=0
for j in range(n):
    for i in range(n):
        count=max(count, dfs(i,j))

print(count)