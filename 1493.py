# 박스 채우기

# length * width * height 박스, 한변의 길이는 2의 제곱꼴 
# 입력 - length, width, heigth 가 첫줄, 큐브 종류 수 N이 두번째줄, 
#       세번째줄부터 N개의 줄에 큐브종류 A와 개수 B가 주어짐, 종류는 한 변의 길이를 나타낼 때 쓰는 2^i에서 i
# 출력 - 첫째 줄에 필요한 큐브의 개수의 최솟값을 출력한다. 만약 채울 수 없다면 -1

# 부피랑 개수제한이 있어서 단순이 길이같은거로만 계산하면 하기 힘듦


length, width, height = map(int, input().split())
N = int(input())

cube=[]
for i in range(N):
    a,b=map(int, input().split())
    cube.append([2**a, b])

answer=0
temp=0
# 큰 큐브부터 채워넣도록 하고 개수가 맞을때만 count 올리고 박스 줄이기
# 큐브를 채우면 세구역으로 다시 박스를 나눠줄 수 있음
l,w,h = length, width, height
for j in range(len(cube)-1,-1,-1):
    
    if (l-cube[j][0]>=0 and w-cube[j][0]>=0 and h-cube[j][0]>=0):
        if l: # 개수가 알맞다면 박스 수를 추가 박스수 또는 필요한 개수
            answer+=min(cube[j][1])
    

