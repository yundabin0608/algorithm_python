# 주차장 실버2

# 시내주차장 N개 주차공간 존재, 매일 아침 모두 비어있으며 하룻동안 다음처럼 운영
# 차 도착시 관리인이 빈 공간 검사후 없으면 빈 공간 있을때까지 입구에서 기다리기
# 빈공간이 하나만 있거나 없다가 한대가 떠나면 그장소 주차
# 빈공간 여러곳일 경우 번호가 가장 작은 공간에 주차
# 여러대 차량 도착 시 도착순으로 대기장소에서 기다림 (대기장소는 큐 스타일)
# 주차료 = 챠량의 무게 * 주차공간마다 책정된 단위 무게당 요금

from collections import deque


###???? fee와 weight을 그냥 리스트로 할 경우 답이 나오지 않고 시간초과가 되는데 그 이유는?
###???? parking[spot] = waiting.popleft() 이부분 문제인데 왜그런걸까
###???? 리스트이던 큐이던 원소 찾는것은 똑같이 O(N)이 걸리지 않는가??

N, M = map(int, input().split())
fee = deque([int(input()) for _ in range(N)])
weight = deque([int(input()) for _ in range(M)])
waiting = deque()  # 주차장 차있을 경우 대기 (차번호가 들어감)
parking = [0] * N  # 주차상태
total = 0

for i in range(2*M):
    inout = int(input())
    
    # 차 들어오기
    if inout>0 : 

        # 주차장에 자리 있으면 가장 작은 번호에 주차
        if 0 in parking :  
            for num in range(N):
                if parking[num] == 0:
                    parking[num] = inout
                    break
        
        # 주차장에 자리 없다면
        else :
            waiting.append(inout)

    # 차 나가기
    else : 
        inout = -inout  
        spot = parking.index(inout)   # 주차한 자리 인덱스
        parking[spot] = 0
        total += weight[inout-1] * fee[spot]  # queue의 경우 안의 weight[inout-1] 사용 불가
     
        if waiting :  # 주차장에 차 있으면 차 나간 자리에 기다리는 큐에서 빼서 세우기
            parking[spot] = waiting.popleft()

print(total)


        
     



    
    
    

    
    

    
