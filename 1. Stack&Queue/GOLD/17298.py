# 오큰수

# 크기 N인 수열 A,(A1~An)
# 수열 각 원소 Ai에 대해 오큰수 NGE(i)를 구할것 (오큰수는 오른쪽에 있으면서 Ai보다 큰수중 가장 왼쪽, 없으면 -1)

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int,input().split()))
stack = deque()
result = [-1]*N

for i in range(N):
    while stack and stack[-1][0] < A[i]:
        num, idx = stack.pop()
        result[idx] = A[i]
    stack.append((A[i], i))

print(*result)

# 왼쪽에서부터 값을 스택에 넣으면서 진행
# 값을 넣을때 스택안에 자기보다 작은수가 없을때까지 pop한 후 넣기
# 즉 스택에 쌓다가 더큰수 나오면 없애고 큰거만 다시 넣기 그리고 스택에 있던 숫자들 오큰수를 현재 큰수로 변경
# 3 5 2 7
# 3|
# 5|  (3<5이므로 NGE(1)=5)
# 5|2
# 7|  반복 (NGE(2)=7, NGE(3)=7) 
# 인덱스에 맞는 NGE 찾기위해 i 넣고, 새로 넣는 수 대소 비교 위해 A[i] 넣기