# 고정점 찾기

# 고정점은 수열의 원소중 그 값이 인덱스와 동일한 원소를 의미
# 하나의 수열이 N개 서로다를 원소 포함, 모든원소는 오른차순 정렬
# 이때, 고정점이 있으면 출력 없으면 -1 출력

sequence = list(map(int, input().list()))


def binary_search(array, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==mid:
        return mid
    # 수열의 중간인덱스보다 중간인덱스 값 클 경우 중간이후부분은 볼 필요없음
    elif array[mid]>mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)

index = binary_search(sequence, 0, len(sequence)-1)

if index == None:
    print(-1)
else:
    print(index)
