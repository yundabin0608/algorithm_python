# 트럭

# 한 다리 한 차선위로 n개 트럭이 지나가며 이때 다리 위대 W대 트럭만 올라갈 수 있다.
# 트럭 순서는 못바꾸며 무게는 서로 같지 않을 수 있다.
# 다리 길이는 W단위길이이며, 각 트럭들은 하나의 단위 시간에 하나의 단위길이만큼 이동가능
# 이때 다리 위에 올라간 트럭들 무게 합은 최대 하중인 L보다 작거나 같아야 함.

from collections import deque

n,w,L = map(int, input().split())
trucks = list(map(int, input().split()))
trucks = deque(trucks)
time = 0

bridge = deque([0 for _ in range(w)]) # 다리 길이는 w

while bridge :
    
    bridge.popleft()
    time += 1
    
    if trucks :
        tw = trucks.popleft()
        
        # 다리 위 무게 측정
        cSum = 0
        for i in range(len(bridge)):
            cSum += bridge[i]
        
        if cSum + tw <= L:      # 차 진입 가능하면 다리위로 차 올리기
            bridge.append(tw)
        else:                   # 차 진입 불가하면 뽑았던 트럭 다시 큐 원래 자리로 넣고 (appendleft) 다리에 0 올리기
            trucks.appendleft(tw)
            bridge.append(0)
    
print(time)
    
        
        