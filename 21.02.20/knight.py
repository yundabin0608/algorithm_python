# 체스판의 행렬 리스트화
row = ['1', '2', '3', '4', '5', '6', '7', '8']
colum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 움직일 수 있는 방향 8가지 설정
move_dx = [ -2, -2, 2, 2, -1, 1, -1, 1]
move_dy = [ -1, 1, -1, 1, -2, -2, 2, 2]

#입력값 변환
data = input()
d_colum = data[0]
d_row = int(data[1])

# 입력 위치 숫자 좌표계로 표현
location = [0, 0]
for i in range(8):
    if (d_colum == colum[i]):
        location[0] == i+1
    if (d_row == row[i]):
        location[1] ==i+1

# 나동빈씨는 그냥 입력받아서 location 안쓰고 colum을 ord써서 표현했다. 나는 좌표계로 표현

# 8가지의 경우의 수 테스트 후 결과값 출력
answer = 0
for i in range(8):
    if ((location[0]-move_dx[i] > 0 and location[0]-move_dx[i] < 9)
    and(location[1]-move_dy[i] > 0  and location[1]-move_dy[i] < 9)):
        answer += 1
    
print(answer)
