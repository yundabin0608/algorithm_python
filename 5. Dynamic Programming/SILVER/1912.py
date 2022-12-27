# 연속합

# 임의의 수열이 주어지고, 이중 연속된 몇개의 수의 합의 최댓값 구할것

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
    nums[i] = max(nums[i], nums[i-1]+nums[i])

print(max(nums))