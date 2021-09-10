# 숨바꼭질 
# 수빈 : 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생 : 점 K(0 ≤ K ≤ 100,000) 
# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 입력 : 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 출력 : 수빈이가 동생을 찾는 가장 빠른 시간

from collections import deque

N, K = map(int, input().split())
find = [0] * 100001

def bfs():
    q = deque()
    q.append(N)

    while q:
        now = q.popleft()

        if now == K:
            return find[now]

         # 여기부분을 해결 못했어서 답지봤음..ㅋㅋㅋ 나는 조건문으로 세개 나눴다가 실패함 이렇게 푸는게 더 효율적일것 같넹
         # 이부분을 떠올리는게 키포인트인듯
        for next in (now+1, now-1, 2*now):
            if (0 <= next < 100001) and find[next] == 0:
                find[next] = find[now] + 1   # 거리리스트에 이전거리+1로 갱신
                q.append(next)
 
print(bfs())

# 재귀로 하는방법!!
# def c(n,k):
#     if n>=k:
#         return n-k
#     elif k == 1:
#         return 1
#     elif k%2:
#         return 1+min(c(n,k-1),c(n,k+1))
#     else:
#         return min(k-n, 1+c(n,k//2))
    
# n, k = map(int,input().split())
# print(c(n,k))
