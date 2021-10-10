# 공주님의 정원
# 시간초과나서 입력방식도 바꿨는데 계쏙 이럼 ㅜㅜㅜㅜ
# days는 이런늒임 [[2, 15, 3, 23], [4, 12, 6, 5]]
# 최소한으로 꽃 심으려면 꽃이 지기전에 심으면 되고 이전 꽃이 지고나서 지면 됨

# 3~11월까지가 범위임 (1차 반복) 날짜가 11월 30일 이하이면 (while 반복 혹은 for 반복, 2차 조건및 반복)
# 꽃이 지는날들을 적고 (같은날에 피면 그중에 늦게지는 놈 하나만 살리기) => 꽃[피는날]=[지는날]로 기록
# 기간안에 있으면 count 증가시키고 음... 그 불가능할때는 어카지..?


N = int(input())
days = []
for i in range(N):
    days += [list(map(int, input().split()))]

count = 0
start = [3, 1]   # 꽃이 피는날 (매번 갱신)
end = [3, 1]     # 꽃이 지는날 (매번 갱신)
check = []

# k는 꽃 하나하나를 나타내고 j는 그꽃의 날짜를 
for k in range(N):
    for j in range(N):
        if ((days[j][0] < start[0]) or (days[j][0] == start[0] and days[j][1] <= start[1])) and ((days[j][2] > end[0]) or (days[j][2] == end[0] and days[j][3] >= end[1])):
            check = days[j]
            end = [days[j][2], days[j][3]]
    if [check[2], check[3]] == [start[0], start[1]]:
        break
    elif check:
        count += 1
    elif count == 0:
        count=0
        break
    start = [check[2], check[3]]
    check = []

print(count)


import sys 
# 월과 월별 일수 누적한 값

accumulation={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334} 

def md_to_d(month, day): 
    return accumulation[month]+day 

flowers=[] 
N=int(sys.stdin.readline()) 
for i in range(N): 
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split()) 
    flowers.append((md_to_d(start_month, start_day), md_to_d(end_month, end_day))) 

selected=[] 
start, end, startdate, enddate = 0, 60, 60, 334
flowers.sort(key=lambda x:(x[0], x[1])) 
# 시작 날짜 기준으로 정렬 -> 만약 같은 날짜에 시작하면 일찍 끝나는 꽃이 우선이 되도록 정렬
x, temp, changed = -1, 0, 0
selected=[] 
while end<=enddate and x<N: 
    changed=0 
    x+=1 
    # x는 계속 증가하면서 꽃들 탐색하고 changed는 매번 0으로 갱신
    for i in range(x, N): 
        if flowers[i][0]>end: 
            break 
            # 지금 심은게 뒤에있는거보다 늦게 질 경우
        if temp<flowers[i][1]: 
            temp=flowers[i][1] 
            x=i 
            changed=1 
    if changed==1: 
        end=temp 
        selected.append(flowers[x]) 
    else: 
        selected=[] 
        break 
print(len(selected))

