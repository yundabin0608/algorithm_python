# 유기농 배추 (런타임에러)
# 배추흰지렁이는 해충을 잡으며 상하좌우로 이어진곳 하나당 하나의 배추 흰지렁이가 필요
# 입력은 배추밭 가로세로길이와 배추가 심어져있는 위치 개수K, K번만큼 위치들의 좌표 입력
# 출력은 필요한 최소 배추 흰지렁이마리수 1: 배추있 0:없
# 재귀 제한높이 설정하지 않으면 런타임에러뜸
import sys
sys.setrecursionlimit(50000)

# answer값이 1일경우만 answer값을 변경해주고 1일경우에만 상,하,좌,우 dfs 재귀호출
# def dfs(x,y):
#     if answer[y][x]==1:
#         answer[y][x]+=1 
#         # 상,하,좌,우 위치 모두 재귀호출
#         if (x-1)>0: dfs(x-1,y)
#         if (x+1)<M: dfs(x+1,y)
#         if (y-1)>0: dfs(x,y-1)
#         if (y+1)<N: dfs(x,y+1) 

# T=int(input())
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# for i in range(T):
   
#     M,N,K= map(int, input().split())
#     count=0
#     cabbage=[]
#     answer= [[0]*M for _ in range(N)]
    
#     # cabbage리스트에 1인 좌표 넣고 answer도 1과 0으로 바꿈
#     for i in range(K):
#         cabbage.append(list(map(int, input().split())))
#         x,y=cabbage[i][0], cabbage[i][1]
#         answer[y][x]=1
    
#     # cabbage 리스트에서 해당하는 좌표의 answer이 1일 경우에만 dfs 수행
#     for x,y in cabbage:
#         if(answer[y][x]==1):
#             dfs(x,y)
#             count+=1    
#     print(count)
    
# dfs를 이용해서 양배추 리스트의 좌표들을 갈수있는데까지 이동하도록 answer리스트는 1로 바꾸기 ,dfs 호출할때마다 count+1하기
# 자꾸 틀리거나 런타임에러나서 변형한 밑에 답

def dfs(x, y): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
 
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        if (0 <= nx < N) and (0 <= ny < M): 
            if matrix[nx][ny] == 1: 
                matrix[nx][ny] = -1 
                dfs(nx, ny) 
                
T = int(input()) 
for _ in range(T): 
    M, N, K = map(int, input().split()) 
    matrix = [[0]*M for _ in range(N)] 
    cnt = 0 
    
    for _ in range(K): 
        m, n = map(int, input().split()) 
        matrix[n][m] = 1 
    
    for i in range(N): 
        for j in range(M):  
            if matrix[i][j] > 0: 
                dfs(i, j) 
                cnt += 1 
    print(cnt)