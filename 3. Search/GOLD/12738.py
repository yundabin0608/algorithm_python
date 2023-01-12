# 가장 긴 증가하는 부분수열3

# 수열 A가 주어질 땨, 가장 긴 증가하는 부분증가수열 구할것

import sys
input = sys.stdin.readline
from bisect import bisect_left
# 해당 값이 리스트에 있다면 index를 반환하고
# 값이 리스트에 없다면 오름차순에 들어갈 index 반환함

N = int(input())
A = list(map(int, input().split()))
tmp = []

for a in A:
    k = bisect_left(tmp, a)
    if len(tmp)<=k:
        tmp.append(a)
    else :
        tmp[k] = a

print(len(tmp))


# dp로 길이를 구하려니 시간초과가 떠서 이분탐색 이용함
# 조건은 k개의  수가 들어왔을때 tmp의 가장 큰 k번째만 신경쓰면 되므로
# 왜냐면 길이가 길어지기 위해 이보다 큰 수가 들어와야 하므로
# 즉 k보다 앞선 것들의 숫자 순서는 바뀌어도 상관 없음
# 주어진 리스트의 수들을 하나씩 보면서
# 만약 이 수가 tmp에 있는 수들보다 크다면 dp의 맨 마지막에 추가하고
# 아니라면, 자신보다 큰 수들중에서 가장 작은 값과 바꿈