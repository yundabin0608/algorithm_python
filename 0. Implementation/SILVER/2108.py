# 통계학

# 줄의 개수가 주어짐 ( N = 1~5000000, 홀수)
# 산술평균, 중앙값, 최빈값(여러개면 두번째로 작은 값), 범위(최대-최소) 를 각 줄에 출력

import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()

print(round(sum(num)/N))
print(num[N//2])

common = Counter(num).most_common(2)
if N>1 and common[0][1] == common[1][1] : print(common[1][0])
else : print(common[0][0])

print(max(num)-min(num))