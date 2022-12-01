# 종이의 개수

# N*N 행렬을 규칙에 맞게 자를것
# 종이가 모두 같은수면 그대로 쓰고 아니면, 종이를 같은크기 9개로 자르고 같은수면 stop
# 각 -1, 0, 1로만 채워진 종이의 개수를 구할것

import sys
input = sys.stdin.readline

paper = []
answer = [0]*3
N = int(input())
for _ in range(N):
    paper.append(list(map(int, input().split())))

def cut(x,y,n):
    global answer
    # 종이에 다른수가 없는지 확인 만약 있다면 9조각으로 자르기
    standard = paper[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if paper[i][j] != standard:
                for a in range(3):
                    for b in range(3):
                        cut(x+a*n//3,y+b*n//3,n//3)
                return
    
    if standard == -1: answer[0]+=1
    elif standard ==0: answer[1]+=1
    else :             answer[2]+=1

cut(0,0,N)
print(*answer, sep="\n")