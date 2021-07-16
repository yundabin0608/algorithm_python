# 개똥벌레

# 동굴길이 N, 높이 H,첫 장애물 석순->종유석->석순 반복
# 개똥벌레는 장애물 피하지않고 일직선으로 가면서 장애물 파괴함
# 파괴해야하는 장애물 최솟값, 그러한 구간의 개수

N,H=map(int, input().split())
obstacle=[int(input()) for _ in range(N)]

# 종유석과 석순들의 길이
j=[]
s=[]

for i in range(N):
    if i%2==0:
        j.append(obstacle[i])
    else:
        s.append(obstacle[i])

