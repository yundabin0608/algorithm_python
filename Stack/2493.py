# 탑 - 스택이용

# 6 9 5 7 4 이런식이면
# 첫번째 스택에 없고 높이는 6 따라서 수신가능탑 없음 0
# 두번째 스택에 [0,6] 있고 높이는 9 9>6 이므로 6,0 뺌. 스택 비었으므로 수신가능탑 없음 0
# 세번째 스택에 [1,9] 있고 높이는 5 5<9 이므로 수신가능한 탑은 (1+1=2), 5,2 스택넣기
# 네번째 스택에 [[1,9],[2,5]]있고 높이 7 7>5 이므로 이거 빼고 7<9 이므로 수신탑은 2, 7,3 스택넣기
# 다섯번째 스택에 [[1,9],[3,7]]있고 높이 4 4<7 이므로 수신가능탑 (3+1=4)

N=int(input())
height = list(map(int, input().split()))
stack = []
answer=[0 for i in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1]>height[i]: # 스택의 맨위꺼랑 높이 비교
            answer[i]=stack[-1][0]+1
            break
        else:
            stack.pop()
    stack.append([i, height[i]])

for k in range(N):
    print(answer[k], end=" ")