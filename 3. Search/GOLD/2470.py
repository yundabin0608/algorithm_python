# 두 용액

# 산성 용액 특성값은 1 ~ 1,000,000,000 
# 알칼리성 용액 특성값은 -1 ~ -1,000,000,000
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용딘 각 용액 특성값 합으로 정의
# 주어진 용액들 중 두개의 서로 다른 용액을 혼합해 특성값이 0에 가장 가까운 용액 만들기

import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

front, back = 0, N-1
answer = sys.maxsize
result = []

while front < back:
    tmp1, tmp2 = solution[front], solution[back]
    tmp3 = tmp1 + tmp2
    sol_sum = abs(tmp3)

    if sol_sum < answer:
        answer = sol_sum
        result = [tmp1, tmp2]
    
    # 용액합 음수면 합이 더 크도록 (0에 가까워지게) front를 하나 앞으로 옮기고 양수면 반대
    if tmp3 <0: front += 1
    else : back -=1

print(result[0], result[1])