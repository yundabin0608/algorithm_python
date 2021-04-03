# 부품찾기
# 손님이 M개 종류 부품 대량 구매하겠다는 견적서 부품은 N개 있음
# 이때 가게 안에 M개 종류 모두 확인해 부품 모두 있는지 확인

# 이진탐색 함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid=(start+end)//2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작으면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)


N = int(input())
parts=list(map(int, input().split()))
M = int(input())
req = list(map(int, input().split()))

parts.sort()

for i in range(M):
    num=req[i]

    result=binary_search(parts, num, 0, N-1)
    if result == None:
        print("No", end=" ")
    else:
        print("yes", end=" ")

print()
