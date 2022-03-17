# 가희와 은행

# 손님 정보 x번 손님의 id 값은 px, 업무처리에 필요한 시간 tx, 영업시작후 cx후 들어옴
# 손님은 은행에 들어옴과 동시에 대기 큐 맨 뒤에 섬

# 대기 큐 맨앞 고객이 x번이면 직원은 tx>T이면 x번손님 업무 T초 처리. 그후 x번 손님 처리업무 시간은 tx-T
# tx<T이면 x번 손님 업무 처리후 그 손님 업무에 필요한 시간은 0이 됨
# 대기 큐 맨 앞에 있는 고객인 x번 손님은 tx=0이면 은행 밖으로 다가며 아니면 대기 큐 맨 뒤로 이동. 이때 도착한 손님 있으면 그뒤로
# 대기 큐에 고객 남아있으면 위의 과정 반복
# 엄무 시작한 시점으로부터 0초가 지났을때부터 W-1초가 지났을때까지 창구에 있는 직원이 어떤 고객의 업무를 처리하는지 알려주시오

from collections import deque

N,T,W = map(int, input().split())
waiting = deque()

# 이미 기다리는 손님
for _ in range(N):
    p,t = map(int, input().splite())
    waiting.appendleft((p, t))

# 오픈 후 오는 손님
after = []
M = int(input())
for _ in range(M):
    p,t,c = map(int, input().splite())
    after.append((p,t,c))
after.sort(key=lambda x:x[2]) # 오는 시간순 정렬
now = 1

while waiting and now<W:
    
    cutom_p, custom_t = waiting.popleft()
    
    if custom_t >= T:
        # 고객 T만큼 만나기
        
        # 만나는 동안 들어온 고객 있으면 줄 서게 하기
        # 고객의 일이 남았으면 뒤로가서 줄서게 하기
        print()
    else:
        # 고객 필요한 시간만큼 고객 만나고
        # 만나는 동안 고객 들어온거 있으면 줄서게 하기
        print()
        
    
    