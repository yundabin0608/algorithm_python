# 상근이의 여행

# 가장 적은 종류의 비행기를 타고 모든 국가를 여행하려 함.
# 상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가(이미 방문국가도 O)를 거쳐가도 가능 

import sys
input = sys.stdin.readline

T=int(input())

# index 번째 나라 방문하도록 함 => result[index]=1
# index 번째 나라를 가는 비행기들 번호를 
def dfs(index, cnt):
    result[index]=1
    for i in planes[index]:
        if result[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

for _ in range(T):
    N,M = map(int, input().split())
    planes=[[] for _ in range(N)]
    result = [0]*N
    for _ in range(M):
        a, b = map(int, input().split())
        planes[a-1].append(b-1)
        planes[b-1].append(a-1)
        
    count = dfs(0,0)
    print(count)
        
        
    