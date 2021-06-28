N, M = map(int, input().split())
A, B, d = map(int, input().split())
answer = 0

# 육지 바다 정보가 담긴 게임보드 생성 (N*M size)
gameboard=[]
for i in range(N):
    gameboard.append(list(map(int,input().split())))

# 방향을 바꾸는 함수 
def rotation(dir) :
    if (dir == 0) :
        d=3
        return d
    else :
        return d-1

# 북 동 남 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 게임캐릭터 맵에 입장
gameboard[A][B]=2
answer=1


while True:
    move_count=0  #움직인 회수 세어줌 
    rotation(d)

    #캐릭터 왼쪽 한번도 못가봄
    if (gameboard[A+dx[d]][B+dy[d]]== 0): 
        gameboard[A+dx[d]][B+dy[d]]==2    #2는 육지방문
        A+=dx[d]
        B+=dy[d]
        answer+=1
        d=rotation(d)
        move_count=0
    else:
        move_count+=1
    
    #캐릭터 사방이 바다 혹은 가본경우
    if (move_count==4):
        move_count=0


print(answer)

