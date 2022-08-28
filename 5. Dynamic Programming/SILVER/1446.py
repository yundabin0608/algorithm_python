# 지름길

# D킬로 미터 고속도로에 지름길이 존재하며 일반통행이고 고솔도로를 역주행할 수는 X
# 세준이가 운전해야 하는 거리의 최솟값

import sys
input = sys.stdin.readline

# 지름길과 고속도로 길이// N<12, D<10000 
N, D = map(int, input().split())
# 시작, 도착, 지름길 길이
road = [list(map(int, input().split())) for _ in range(N)]

shortest = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        # Dp 느낌, 
        shortest[i] = min(shortest[i], shortest[i-1]+1)
    for start, finish, len in road:
        if i == start and finish <= D and shortest[i]+len < shortest[finish]:
            shortest[finish] = shortest[i]+len
print(shortest[D])