# 나무 자르기

# 절단기 높이 H를 지정하면 땅으로부터 H미터 위로 올라가서 그 줄의 연속한 나무를 모두 절단
# 상근이는 나무를 필요한 만큼 집으로 가져갈 것.
# 적어도 M 미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이 최대값 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

H, front, back = 0, 1, max(trees)
while (front <= back):

    mid = (front+back)//2
    cuttings = 0
    for h in trees:
        if h > mid : 
            cuttings += h-mid
            if cuttings > M : break  # 추가 안하면 시간초과됨
    
    if cuttings >= M :
        H=mid
        front = mid+1
    else:
        back = mid-1

print(H)