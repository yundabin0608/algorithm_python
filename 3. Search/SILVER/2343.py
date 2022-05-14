# 기타 레슨

# 블루레이에는 N개의 강의가 있으며 녹화시 강의의 순서가 바뀌면 안됨
# 블루레이의 개수는 가급적으로 적어야 하며 M개의 블루레이에 모든 기타 강의 동영상 녹화할것
# 블루레이의 크기(녹화 가능 길이)는 최소화 하며 M개의 블루레이는 모두 같은 크기
# 가능한 블루레이 최소 크기

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
lectures = list(map(int, input().split()))

result, front , back = 1, max(lectures), sum(lectures)
while (front<=back):

    mid = (front+back)//2
    # 블루레이 나눠 담을때, 몇조각 나오는지 record에 저장
    # 원하는 갯수보다 record 많으면 블루레이 크기 늘임 적으면 크기 줄임
    # tmp는 블루레이 1개에 구간구간 총 들어가는 양
    records, tmp =0,0
    for i in range(N):
        if tmp + lectures[i] > mid :
            records+=1
            tmp = 0
        tmp += lectures[i]
    records +=1 if tmp else 0

    if records<=M:
        back = mid-1
        result = mid
    else:
        front = mid+1

print(result)
