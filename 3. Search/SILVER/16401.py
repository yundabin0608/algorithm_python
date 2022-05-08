# 과자 나눠주기

# 모든 조카에게 같은 길이의 막대과자 주며, M명의 조카, N개의 과자 존재
# 조카 1명에게 줄 수 있는 막대 과자의 최대 길이 구할것
# 막대과자는 길이와 관계없이 여러 조각으로 나눠질 수 있지만 하나로 합칠순 없고 길이는 양의 정수

# 그냥 이진탐색 코드 거의 그대로 이용

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
length = list(map(int, input().split()))
result = 0

# 자르는 막대기 길이는 막대수 상관 없이 막대기들의 최대높이에서 1 사이면 되니까
front = 1
back = max(length)
while (front <= back):
    mid = (front+back)//2
    # 막대기 자른것들 합 예로 목표 5이고 막대 1,3,5,7,9 이면 5짜리 막대는 3개 (=cut_bar)
    cut_bar=0
    for l in length:
        cut_bar += l//mid 
    if cut_bar >= M:
        result = mid
        front = mid+1
    else:
        back = mid-1
print(result)