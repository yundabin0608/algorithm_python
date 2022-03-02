# 체스판 다시 칠하기

# M*N 크기의 보드에서 어떤 정사각형은 검은색 또는 흰색임
# 이 보드를 잘라 8*8크기 체스판을 만들것 
# 체스판은 검흰 번갈아 칠해져야할것, 변을 공유하는 두 사각형은 다른색으로 칠해질것

# 입력 : 첫줄 N,M (8~50 자연수), 둘째줄부터 N줄에 보드 상태 B:검 W:흰
# 출력 : 첫줄에 지민이가 다시 칠할 정사각형 개수 최솟값 출력

# 부루트포스로 모든 경우수 돌려 최적해 구하기

N,M = map(int, input().split())
list = []
count = []

for _ in range(N):
    list.append(input())

# 체스판에서 시작점
for i in range(N-7):
    for j in range(M-7):
        # 체스판 시작이 흰색일경우와 검은색일경우 나누기 위해
        W_idx = 0
        B_idx = 0
        # 시작점 부터 8*8 체스판 끊어내기
        # OXOXOXOX --> ex) x=1,y=1 이랑 x=3,y=2 이것처럼 짝수는 시작점 동일
        # XOXOXOXO --> ex) x=1,y=2 이랑 x=4,y=1 이것처럼 홀수는 시작점 반대
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2 == 0 :
                    if list[x][y]== 'W': 
                        B_idx +=1
                    if list[x][y]== 'B': 
                        W_idx +=1
                else :
                    if list[x][y]== 'W': 
                        W_idx +=1
                    if list[x][y]== 'B': 
                        B_idx +=1
        count.append(W_idx)
        count.append(B_idx)
print(min(count))
