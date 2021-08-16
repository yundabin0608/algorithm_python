# 공주님의 정원
# 시간초과나서 입력방식도 바꿨는데 계쏙 이럼 ㅜㅜㅜㅜ

import sys
N = int(input())
days = []
for i in range(N):
    days += [list(map(int, sys.stdin.readline().split()))]

count = 0
start = [3, 1]
end = [3, 1]
check = []
for k in range(N):
    for j in range(N):
        if ((days[j][0] < start[0]) or (days[j][0] == start[0] and days[j][1] <= start[1])) and ((days[j][2] > end[0]) or (days[j][2] == end[0] and days[j][3] >= end[1])):
            check = days[j]
            end = [days[j][2], days[j][3]]
    if [check[2], check[3]] == [start[0], start[1]]:
        break
    elif check:
        count += 1
    elif count == 0:
        count=0
        break
    start = [check[2], check[3]]
    check = []

print(count)