# 탑

# 레이저는 지표면과 평행하게 왼쪽으로 발사되며, 발사된 신호는 가장 먼저 만나는 하나의 탑에서만 수신 가능
# 탑의 수 N (1~5000000), 탑들 높이 (1~100000000)
# 각 탑들에서 발사한 레이저 신호를 수신하는 탑들 번호 없으면 0

N=int(input())
height = list(map(int, input().split()))

answer=[-1]*5000000

# 인덱스 역순으로 돌아다닐것
for i in range(N-1,-1,-1):
    tap=height[i]
    for j in range(i-1, -1, -1):
        if answer[i]!=-1 : break
        if(tap<height[j]):
            answer[i]=(j+1)
    if (answer[i]==-1): 
        answer[i]=0
    

for k in range(N):
    print(answer[k], end=" ")
