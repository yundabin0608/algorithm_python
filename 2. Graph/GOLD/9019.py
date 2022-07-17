# DSLR

# 간단한 계산기에서 D,S,L,R 계산 수행하며 계산기엔 레지스터 하나있으며 0~9999 수 저장가능
# 레지스터의 숫자 d1,d2,d3,d4 변환 -> n = 1000d1 + 100d2 + 10d3 + d4

# D: 2*n n>9999이면 10000 으로 나눈 나머지(2n mod 10000) 저장
# S: n-1 n이 0 이라면 9999 저장
# L: n의 각 자릿수를 왼편으로 회전 (왼편부터 d2, d3, d4, d1)
# R: n의 각 자릿수를 오른편으로 회전 (왼편부터 d4, d1, d2, d3)

# 숫자 A, B가 주어지면 둘은 초기값과 최종값이므로 최종값이 되기 위해 필요한 최소 명령어 나열 출력할 것

# 틀림 BFS로 해보래

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    A, B = map(int, input().split())
    queue = deque()
    queue.append((A,""))
    visited = [0]*10000

    while queue:
        num, answer = queue.popleft()
        visited[num] = 1

        if num == B:
            print(answer)
            break

        D = (2*num)%10000
        if visited[D]==0:
            queue.append((D, answer+"D"))

        S = 9999 if (num-1)==0 else num-1
        if visited[S]==0:
            queue.append((S, answer+"S"))

        L = (10*num)%10000+(num//1000)  # 1234 => 2341 (234*10 + 1)
        if visited[L]==0:
            queue.append((L, answer+"L"))

        R = num//10+(num%10)*1000 # 1234 => 4123 (1230/10 + 4*1000)
        if visited[R]==0:
            queue.append((R, answer+"R"))