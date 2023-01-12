# 가장 큰 증가 부분 수열

# 수열이 주어질때 증가 부분 수열중 가장 합이 클때의 값 구하기

import sys
input = sys.stdin.readline

A = int(input())
nums = list(map(int, input().split()))

for i in range(A):
    tmp = nums[i] # 갱신될 수 있으니 사전에 값 받아두기
    for j in range(i):
        if nums[i]>nums[j]:
            nums[i] = max(nums[i], nums[j]+tmp)

print(max(nums))



