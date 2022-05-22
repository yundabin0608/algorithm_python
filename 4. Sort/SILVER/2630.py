# 색종이 만들기

# 정사각형 종이는 하얀색 또는 파란색으로 칠해져 있음
# 위의 종이를 일정 규칙으로 잘라 다양한 크기의 정사각형 모양의 하얀 또는 파란 색종이 만들것
# 전체 종이가 모두 같은색으로 칠해지지 않았다면 가로, 세로 중간 잘라 나눔 (반복)
# 잘라진 하얀색, 파란색 종이 개수 출력

import sys
input = sys.stdin.readline

N = int(input()) # 2,4,8,16,32,64,128 중 하나// 0:흰 1:파
paper =[list(map(int, input().split())) for _ in range(N)]

white, blue = 0,0

def test(x,y,N):
    check = paper[y][x]
    for i in range(y,y+N):
        for j in range(x,x+N):
            if check != paper[i][j]:
                # 종이가 단색 아니라면 4개로 쪼개
                test(x,y,N//2)
                test(x+N//2,y,N//2)
                test(x,y+N//2,N//2)
                test(x+N//2,y+N//2,N//2)
                return
    
    global white, blue
    if check ==0 : white+=1
    else: blue+=1

test(0,0,N)
print(white)
print(blue)
