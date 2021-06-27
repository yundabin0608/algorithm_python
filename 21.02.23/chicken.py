N, M = map(int, input().split())

#거리 함수
def distance(x1,y1,x2,y2):
    result = abs(x1-x2) + abs(y1-y2)
    return int(result)

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

# 치킨집 M개 고르기 -> 치킨집 우선순위 결정
chic_priority=[]
for i in range(len(chicken_store)):
    c_sum=0
    for j in range(len(house)):
        c_sum+=distance(house[i][0], chicken_store[j][0], 
        house[i][1], chicken_store[j][1])
    chic_priority.append(c_sum)  #이게 잘못된듯 어디다가 붙여가지고 하는겨??
for i in range(M):
    index=-1
    min=9999
    for j in range(len(chic_priority)):
        if(min>chic_priority[j]):
            min=chic_priority[j]
            index=j
    chic_priority.remove(chic_priority[index])
    chicken_store.remove(chicken_store[index])
    #이중리스트 삭제한느법?        

# 치킨집 없앤후 최소 거리 구하기
cal_d=[]
for i in range(len(house)):
    cal_d.append([])
    for j in range(M):
        cal_d[i].append(distance(house[i][0], chicken_store[j][0], 
        house[i][1], chicken_store[j][1]))

answer=0
for i in range(len(house)):
    answer+=min(cal_d[i])
print(answer)