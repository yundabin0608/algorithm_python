# 공유기 설치하기
# 집에 공유기 c개설치. 한집엔 공유기 1대씩 가능
# 가장 인접한 두 공유기 사이 거리 최대가 되게 C개 공유기 N개 집에 설치

N, C = map(int,input().split())
house =[]
for _ in range(N):
    house.append(int(input()))

house.sort()

min = 1
max = house[-1] - house[0]

while(max>=min):
    gap = (min+max)//2

    count=1
    h=house[0]  # 첫번째에 공유기 세우기 , count는 공유기 수

    
    for i in range(1,N):
        if house[i]>= h+gap: # 간격에 맞는 집에 공유기 세우고 (위치가 간격보다 넓으면 집에 공유기 세우기)
            count+=1
            h=house[i]        # 공유기가 최근에 설치된 집갱신

    if count<C:
        max = gap - 1
    elif count >= C:
        min = gap + 1
        answer = gap
print(answer)

# 공유기 설치 할 수 있는 최대+최소//2 에서 간격 시작
# 중간값으로 공유기 설치했을때, 설치 공유기 부족하면 간격 좁혀 공유기 갯수 늘이기.
# 공유기가 많거나 같으면 간격 늘려서 덜 설치/ 최대간격 => 갯수 줄이기 넓히기
#     이 경우 while문 종료될 수 있으므로 answer에 gap 넣어준다.
