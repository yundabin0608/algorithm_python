#감시피하기 

import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
maps = []
empty, teachers = [], []
dx, dy = [1,-1,0,0], [0,0,1,-1]

for y in range(N):
    maps.append(list(input().split()))
    for x in range(N):
        if maps[y][x] == 'X': empty.append([x, y])
        elif maps[y][x] == 'T': teachers.append([x, y])
 
# 벽세우기 
for wall in combinations(empty, 3):
    for x,y in wall: maps [y][x] = 'O'
    flag = False

    for t in teachers:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            while 0<=nx< N and 0<=ny< N and maps[ny][nx] != 'O':
                if maps[ny][nx] == 'S': # 학생일경우
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
 
    if not flag:
        print('YES') # 감시 피한것
        exit()
 
    for y, x in wall: # 다음을 위해 세운 벽 다시 없애기
        maps[y][x] = 'X'
 
print('NO')