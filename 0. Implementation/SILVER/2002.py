# 추월

# 대근이는 차가들어가는 순, 영식이는 차가 터널에서 나오는 순으로 차량번호 적음
# N개의 차량이 지나간 후, 추월했을것으로 여겨지는 차량 몇대인지 출력할 것
# 입력 첫줄은 차의 대수(1~1000), N줄은 대근이 차량번호, 그 후 N줄은 영식이 차량번호

import sys
input  = sys.stdin.readline
answer = 0

N = int(input())
inCar, outCar = {}, []
for i in range(N):
    inCar[input().rstrip()] = i
for _ in range(N):
    outCar.append(input().rstrip())


for i in range(N-1):
    for j in range(i+1, N):
        # 제일 먼저 들어간 차가 그 후에 들어갔던 차들의 순번보다 크다면 추월 ==> 인덱스 작을수록 가장 먼저 들어감
        #     outCar[i]             outCar[j]
        if inCar[outCar[i]] > inCar[outCar[j]]:
            answer+=1
            break
print(answer)