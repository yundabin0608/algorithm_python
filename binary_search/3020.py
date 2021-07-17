# 개똥벌레 pyp3

# 동굴길이 N, 높이 H,첫 장애물 석순->종유석->석순 반복
# 개똥벌레는 장애물 피하지않고 일직선으로 가면서 장애물 파괴함
# 파괴해야하는 장애물 최솟값, 그러한 구간의 개수

N,H=map(int, input().split())
s=[]
j=[]

for i in range(N):
    if i%2==0:
        s.append(int(input()))
    else:
        j.append(int(input()))

s.sort()
j.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

min, total=N,0
for i in range(1,H+1): #개똥벌레는 가운데니까 0.5
    s_count = len(s) - binary_search(s, i - 0.5, 0, len(s) - 1)
    j_count = len(j) - binary_search(j, H - i + 0.5, 0, len(j) - 1)

    if min == s_count+j_count:
        total+=1
    elif min > s_count+j_count: # 더 작은 최소값 나타나면 갱신
        total=1
        min=s_count+j_count

print(min, total)