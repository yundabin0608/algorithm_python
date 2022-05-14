# 공유기 설치하기

# 집에 공유기 c개설치. 한집엔 공유기 1대씩 가능
# 가장 인접한 두 공유기 사이 거리 최대가 되게 C개 공유기 N개 집에 설치
# 집집마다의 최소거리는 1

import sys
input = sys.stdin.readline

N, C = map(int,input().split())
house =[int(input()) for _ in range(N)]
house.sort()

max_dist, front, back = 0, 1, (house[N-1]-house[0])
while(front<=back):
    mid = (front+back)//2
    
    counting, tmp = 1, house[0] # 0번째집에 공유기 설치한 상태
    for x in house:
        if x-tmp >= mid : # 집 사이 거리가 mid보다 크면 공유기++
            counting+=1
            tmp = x
    
    if counting >= C :
        front = mid+1
        max_dist = mid
    else:
        back = mid-1

print(max_dist)