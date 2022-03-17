# 뱀 (시// 다음주..)

# N*N 보드위, 보드 상하좌우 끝에 벽, 시작시 뱀은 좌측상단위치하며 길이 1, 처음은 오른쪽 향함
# 뱀은 몸길이 늘려 머리 다음칸 위치, 벽 또는 자기 자신 몸과 부딛히면 게임 끝
# 이동시 사과 있으면 그칸 사과는 없어지고 꼬리는 움직이지 않음
# 사과 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비움 (= 몸길이 변화X)
# 사과의 위치와 뱀의 이동경로가 주어질때 게임이 몇초에 끝날지 결정


N = int(input())
K = int(input())
apples = [list(map(int,input().split())) for _ in range(K)]

L = int(input())
directions = []     # C="L": 왼쪽회전 C="D": 오른쪽회전
for _ in range(L):
    X, C= input().split()
    X=int(X)
    directions.append([X, C])
    
