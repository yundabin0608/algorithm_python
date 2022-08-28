# 내려가기

# N줄에 0~9 숫자 3개씩 적혀있으며 내려가기 게임중 첫~마지막줄 도착하는 것
# 처음 적힌 세 숫자중 하나 골라 시작, 그담줄로 가는데 제약조건 존재
# 바로 아래수로 넘어가거나, 바로 아래수와 붙은 수로만 이동 가능한 것
# 이때 최대와 최소 구할것

# 메모리에서 문제가남!
# 슬라이딩 윈도우 기법 생각하는게 포 인 트

import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
max_score, min_score = score, score
for _ in range(N-1):
    x,y,z = list(map(int, input().split()))
    max_score = [x+max(max_score[0],max_score[1]), y+max(max_score), z+max(max_score[1],max_score[2])]
    min_score = [x+min(min_score[0],min_score[1]), y+min(min_score), z+min(min_score[1],min_score[2])]
print(max(max_score), min(min_score))