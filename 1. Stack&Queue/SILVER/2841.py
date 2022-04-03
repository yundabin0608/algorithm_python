# 외계인의 기타연주

# 1 ~ 6 줄인 기타, 각줄은 1 ~ P번의 프렛이 존재 한줄의 여러개 프렛이면 가장 높은 프렛 음(큰수) 발생
# 손가락으로 프렛을 한번 누르거나 떼는것이 한번 움직인것. 손가락의 최소 움직임수 구하기
# break: 반복문 멈추고 loop 밖으로, continue: 다음순번 loop진행, pass: 다음행동 진행 (조건문에서 딱히 넣을 조건 없을 경우나 초기 넣을 값 없을때 사용)
import sys
input = sys.stdin.readline

N,P = map(int, input().split())
stack = [[] for _ in range(6)] # 배열 아닌 딕셔너리를 사용후 입력시 map을 안쓰면 시간이 150ms가량 감소
result = 0


# 다른줄은 신경 끌 것
# 쳐야 할 멜로디가 같은 줄 스택의 것보다 크면 그냥 누르고 작으면 그때까지 빼기

for _ in range(N):
    l, p = map(int, input().split())
    l-=1
    if not stack[l]:
        stack[l].append(p)
        result += 1   
    else :
        if stack[l]:  
            top = stack[l][-1]       
            if top==p: continue
            elif top<p: 
                stack[l].append(p)
                result += 1
            else : 
                while stack[l] and top>p:   
                    stack[l].pop() 
                    result += 1
                    if stack[l]: top = stack[l][-1]
                if stack[l] and top==p: continue
                stack[l].append(p)
                result+=1
        else:
            stack[l].append(p)
            result += 1
        
print(result)


# 간단한 풀이 시간은 얼마 차이 안남
# guitar = {
#     "1": [], "2": [],
#     "3": [], "4": [],
#     "5": [], "6": [],
# }

# count = 0

# for _ in range(N):
#     line, fret = input().split()
#     fret = int(fret)

#     # 주어진 줄의 더 높은 프렛을 누르고 있는 경우, 손가락을 하나씩 뗀다.
#     while guitar[line] and guitar[line][-1] > fret:
#         guitar[line].pop()
#         count += 1

#     # 같은 줄, 같은 프렛인 경우 스킵한다.
#     if guitar[line] and guitar[line][-1] == fret:
#         continue

#     # 주어진 프렛을 현재 줄(= 스택)에 삽입한다.
#     guitar[line].append(fret)
#     count += 1

# print(count)