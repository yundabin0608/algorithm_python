N,M= map(int, input().split())
min_list = []

for i in range(N):
    nums = list(map(int, input().split()))
    min_num = min(nums)

    min_list.append(min_num)

print(max(min_list))
