# 나무자르기

# 절단높이 H 지정 후 그 줄에 연속한 모든 나무 절단
# 나무수 N(1~1000000), 상근이가 집으로 가져가려는 나무 길이 M(1~2000000000)
# 둘째줄에는 나무높이 (높이는 0~1000000000)

# binary search 이용할것
N,H = map(int,input().split())
tree = list(map(int, input().split()))

start=1
end = max(tree)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in tree:
        if x>mid: 
            # 나무 길이가 길어야만 잘리므로
            total += x - mid
            if total>H : break

    # 나무길이가 더 필요하면 많이 자르고 아니라면 적게 자르기
    # total이 H보다 크다는 것은 더많이 잘랐다는것이므로 적게 잘라야 한다는것임 즉 높이를 올려야 적게 잘림
    if total < H: 
        end = mid -1
    else: 
        result = mid
        start = mid+1

print(result)

# 시간초과 발생
# 아마도가져갈 수 있는 나무 길이가 커지면 멈추는 조건 초과하는걸 넣어보자