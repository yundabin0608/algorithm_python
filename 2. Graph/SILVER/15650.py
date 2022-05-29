# N과 M(2)

# 1~N 까지 자연수 중 중복 없이 M개 고른 수열 모두 구할것, 오름차순일 것
# 결과 수열은 중복없이 1줄에 하나씩 나열 그안의 원소들은 띄어쓰기로 구분

import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
result = []
def dfs(start):
    if len(result)==M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(start,N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
dfs(1)

# DFS와 백트래킹를 이용한 기초문제
# 예로 4,2 일때 처음에 dfs(1) -> dfs(2) 호출 (2~N 까지 수중 없는 녀석 넣어줌)
# dfs(2)에서 원소 넣어주고 dfs(3)가면 2개 이미 들어갔으니 출력후 return
# dfs(3)에서 dfs(2)로 돌아오게 되고 pop됨 [1,2]출력 
# dfs(1)에서 dfs(2)|dfs(3)|dfs(4) -> 길이되서 return [1,2]|[1,3]|[1,4]
# dfs(2)에서 dfs(3)|dfs(4) -> return
# ------  -> 여기 크게 도는 부분이 큰 반복문이고 dfs로 가지쳐서 안으로 안으로 들어감