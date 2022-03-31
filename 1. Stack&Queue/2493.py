# 탑

# 일직선 위 N개 높이 다른 탑 왼쪽부터 오른쪽으로 세우고 각 탑꼭대기 레이저 송신기 설치, 건물전체 수신기
# 송신기는 레이저를 왼방향으로 발사, 
# 레이저 신호는 가장 먼저 만나는 탑 1개에서만 수신가능, 탑은 여러개 신호 수신 가능

import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
result = [0 for _ in range(N)]

# 스택이 있다면 이전 스택값의 높이와 지금 들어올 타워의 높이 비교, 없으면 지금 타워 넣기 
# 만약 지금 타워 높이가 더 크면 다음 존재하는 스택값 봐야하므로 pop
# 이전값이 지금 타워 높이보다 높다면 레이저 수신 가능하므로 그때의 인덱스 저장
stack = []
for i in range(N):
    while stack:
        if stack[-1][1]<=towers[i]:
            stack.pop()
        else:
            # 레이저 수신 가능한 타워의 인덱스 저장
            result[i]=stack[-1][0]+1
            break
    stack.append([i, towers[i]])

# 결과 리스트 한번에 출력
print(*result)

# 과정
# 1) 6 stack=[] 이므로 stack[[0,6]]
# 2) 9 stack[[0,6]] 이므로 6<=9 이므로 pop stack[[1,9]]
# 3) 5 stack[[1,9]] 이므로 9>5 따라서 result[2]=2, stack[[1,9],[2,5]](3번째 탑은 2번째 탑이 수신)
# 4) 7 stack[[1,9],[2,5]] 이므로 3<=7이므로 pop 9>7 따라서 result[3]=2, stack[[1,9],[3,7]](4번째 탑은 2번째 탑이 수신))
# 5) 4 stack[[1,9],[3,7]] 이므로 7>4 따라서 result[4]=4
# 끝 result 0부터끝까지 출력 --> 0 0 2 2 4