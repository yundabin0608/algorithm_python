from itertools import combinations
N, M = map(int, input().split())

# 최소 거리 함수
def distance(c,h):
    min_distance=99999
    
    for i in c:
        dist=abs(i[0]-h[0]) + abs(i[1]+h[1])
        min_distance=min(min_distance,dist)
    
    return min_distance

# 도시 정보 입력받음
cmap=[]
for i in range(N):          
    cmap.append(list(map(int, input().split())))

# 치킨집,집 찾아서 좌표를 리스트에 넣기
chicken_store=[]
house = []
for i in range(N):
    for j in range(N):
        if(cmap[i][j]==2):
            chicken_store.append([i,j])
        if(cmap[i][j]==1):
            house.append([i,j])

#치킨집의 조합
chicken_comb = list(combinations(chicken_store,M))

b=[]
for i in chicken_comb:
    t=0
    for j in house:
        t+=distance(j,i)
    b.append(t)

print(min(b))