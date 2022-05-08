# 리모컨

# 리모컨의 숫자 버튼 일부 고장 0~9 + - 버튼이 있음
# +를 누르면 현재 채널에서 +1된 채널, -를 누르면 현재 채널에서 -1된 채널 이동
# 채널 0에서 -누르면 변하지 않고 채널은 무한대 만큼 있음
# 수빈이가 이동하려는 채널은 N이며,여기로 이동하기 위해 최소 몇번 눌러야 하는지. 현재 채널은 100

# 고장나지 않은 숫자들로 target과 가장 가까운 수 찾기
import sys
input = sys.stdin.readline

N = int(input())
result = abs(100-N)

M = int(input())
if M : broken_btt = set(input().split())
else: broken_btt = set()

# 500,000 인데 0에서 올라오는것과 1,000,000 에서 내려오는 경우 있으니 범위 두배
for i in range(1000001):
    for j in str(i): 
        if j in broken_btt:
            break
        # 고장난 버튼 없으면, 해당 숫자 누르는 횟수 + 덧뺄셈 버튼 누르는 수
    else : result = min(result, len(str(i))+abs(i-N))

print(result)