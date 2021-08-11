# 선긋기
# 자의 한 점에서 다른 한 점까지 선그음.이미 선이 있는 위치에 겹쳐그리기 가능
# 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없음
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하기. 선이 여러 번 그려진 곳은 한 번만계산

# 첫째 줄에 선을 그은 횟수 N, 다음 N개의 줄에는 선을 그을 때 선택한 두 점의 위치 x, y (수직선에 긋는다고 생각)

import sys
line_matrix=[]
N= int(input())
answer = 0

for i in range(N): # 입력=>시간초과 (그냥 원래쓰덜데로 하니까 시간초과 -> sys 사용,list(map)을 바로 append 해도 초과)
    X,Y=map(int, sys.stdin.readline().split()) # => x,y 로 받고 이거를 append
    line_matrix.append((X,Y))   
line_matrix.sort() 

prevX, prevY = line_matrix[0][0], line_matrix[0][1]
for i in range(1, N):
    tmpX, tmpY = line_matrix[i][0], line_matrix[i][1]
    if tmpX <= prevY:
        prevY = max(prevY, tmpY)
    else:
        answer+=prevY-prevX
        prevX, prevY = tmpX, tmpY
answer+=prevY-prevX

print(answer)
