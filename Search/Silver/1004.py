# 어린왕자
# 원 = 행성계의 경계, 행성계간 이동은 최대한 피할것
# 은하수 지도, 출발점, 도착점 = input / 어린왕자에게 필요한 최소의 행성계 진입/ 이탈횟수
from math import dist

T = int(input())
for i in range(T):
    start_x, start_y, dest_x, dest_y = map(int,input().split())

    stars_num = int(input())
    stars=[]
    answers=[0]*stars_num
    for i in range(stars_num):
        stars.append(list(map(int, input().split())))

    for i in range(stars_num):
        if (dist((start_x, start_y), (stars[i][0], stars[i][1]))<stars[i][2]):
            answers[i]+=1
        
        if (dist((dest_x, dest_y), (stars[i][0], stars[i][1]))<stars[i][2]):
            answers[i]+=1

    for i in range(stars_num):
        if answers[i]==2:
            answers[i]=0
    
    print(sum(answers))


# 그냥 시작점과 도착점이 행성들안에 있는지 없는지 거리를 통해 구하고 있다면 answer(행성갯수만큼 인덱스지님) 1로 바꿔 
# 나중에 몇개 행성인지는 리스트 원소들의 합을 구하면 나오도록 디자인함
# 해당점이 원 몇개 안에 있는지 중복되는거만 빼고 세어주면 되는거 아니냐고~~~~
# 50% 맞고 나머지 틀림 힝..

# !! 생각해보니까 원에 출발점 도착점이 모두 있으면 그냥 지날필요가 없으므로 빼야함
    