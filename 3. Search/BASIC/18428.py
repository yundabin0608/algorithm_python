#감시피하기 -- combination을 이용한 구현
from itertools import combinations

# 주어진 정보를 담기
direction = [[-1,0],[1,0],[0,-1],[0,1]]
N = int(input())
graph = [[' '] for _ in range(N + 1)]
empty = []
teachers = []
for i in range(1, N + 1):
    graph[i] += input().split()
    for j in range(1, N + 1):
        if graph[i][j] == 'X':
            empty.append([i, j])
        elif graph[i][j] == 'T':
            teachers.append([i, j])
 

 # 남는 빈칸들 중에 3개를 무작위로 뽑아서 벽을 세움 벽은 O
for wall in combinations(empty, 3):
    for y, x in wall:
        graph[y][x] = 'O'
 
    flag = False
    for t in teachers:
        for i in range(4):
            y, x = t
            while 1 <= y <= N and 1 <= x <= N and graph[y][x] != 'O':
                if graph[y][x] == 'S': # 학생일경우
                    flag = True
                    break
                y += direction[i][0]
                x += direction[i][1]
            if flag:
                break
        if flag:
            break
 
    if not flag:
        print('YES') # 감시 피한것
        exit()
 
    for y, x in wall: # 다음을 위해 세운 벽 다시 없애기
        graph[y][x] = 'X'
 
print('NO')