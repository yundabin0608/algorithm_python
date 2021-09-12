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