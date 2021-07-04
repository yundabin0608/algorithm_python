import sys; 
from itertools import combinations
import copy
sys.setrecursionlimit(100000)

# DFS 바이러스가 퍼지는 것을 구현
def dfs(matrix, ck, x, y): #주어진 matrix, check행렬, x, y(바이러스 matrix의 좌표들)
    if ck[x][y] == 0:
        ck[x][y] = 1
        if matrix[x][y] == 0:
            matrix[x][y] = 2
        # dx, dy 하는 것 보다 if로 나누면 조금 더 수행시간이 빠릅니다.
        if x+1 < N and ck[x+1][y] == 0 and matrix[x+1][y] != 1:
            dfs(matrix, ck, x+1, y)
        if x-1 >= 0 and ck[x-1][y] == 0 and matrix[x-1][y] != 1:
            dfs(matrix, ck, x-1, y)
        if y-1 >= 0 and ck[x][y-1] == 0 and matrix[x][y-1] != 1:
            dfs(matrix, ck, x, y-1)
        if y+1 < M and ck[x][y+1] == 0 and matrix[x][y+1] != 1:
            dfs(matrix, ck, x, y+1)
    return matrix

empty_index=[] # empty는 벽을 임의로 세울 combination 결정할때 씀
virus_index=[] 
matrix_in=[]
result = 0

N, M = map(int, input().split())

for i in range(N):
    matrix_in.append(list(map(int, input().split())))
    for j in range(M):
        if matrix_in[i][j]==0:
            empty_index.append([i,j])
        if matrix_in[i][j]==2:
            virus_index.append([i,j])

check = [[0]*M for _ in range(N)] # 바이러스가 이미 퍼졌는지 아닌지 체크하는 용도
# empty_index에서 빈칸중 벽 세울 임의의 3자리 고르는것
for wall in combinations(empty_index, 3):
 
    # 2차원 이상의 다차원 리스트 완전 복사는 copy 모듈의 deepcopy()함수 이용
    V_in = copy.deepcopy(matrix_in)
    cks = copy.deepcopy(check)
    
    # 벽세우기
    for i, j in wall:
        V_in[i][j] = 1

    # 바이러스 퍼뜨리기
    for i, j in virus_index:
        V_in = dfs(V_in, cks, i, j)

    # 안전지대 세기
    count=0
    for i in range(N):
        for j in range(M):
            if V_in[i][j]==0:
                count+=1

    result = max(result, count)

print(result)