n, m = map(int, input().split())
a, b, d = map(int, input().split())

board = []
visit = [[0] * m for _ in range(n)] #방문위치 저장위한 맵 생성해 0으로 초기화
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 위치에서 왼쪽 방향으로 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

# 현재 위치 방문 표시
visit[a][b] = 1

# 이동 시작
cnt = 1
while True:
    d = turn_left(d)
    nx = a + dx[d]
    ny = b + dy[d]
    # 현재 가려는 방향쪽의 칸이 방문하지 않았고 바다가 아닌 경우
    if board[nx][ny] == 0 and visit[nx][ny] == 0:
        # 해당 칸 방문 표시
        visit[nx][ny] = 1
        # 해당 위치로 현재 위치 변경
        a, b = nx, ny
        # 방문 카운트 +1
        cnt += 1
        # 방향 카운트 0으로 초기화
        turn_cnt = 0
        continue
    # 방문 했거나 바다인 경우
    else:
        # 방향 카운트 +1 
        turn_cnt += 1
    
    # 4방향 모두 갔는데 이동하지 못했을 경우
    if turn_cnt == 4:
        # 바라보는 방향을 유지한 채로 뒷 칸의 위치를 생성
        nx = a - dx[d] 
        ny = b - dy[d]
        # 뒤쪽 방향이 바다가 아닌 경우 뒤로 이동
        if board[nx][ny] == 0:
            a = nx
            b = ny
        # 바다인 경우 반복문 종료
        else:
            break
        turn_cnt = 0

# 결과 출력
print(cnt)
