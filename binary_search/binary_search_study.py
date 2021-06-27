# 이진 탐색 소스코드 구현 (재귀함수)
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

# 원소개수랑 찾고자하는 값 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array=list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


# 팁! 많이 쓰이는 파이썬 이진 탐색 라이브러리
# from bisect import bisect_left, bisect_right
# bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽의 인덱스 반환
# bisect_right(a, x) : 동일~~ 오른쪽 인덱스 반환

# 사용 예시) 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 떡볶이 떡 문제
# M을 낮추면 손님이 가져가는 떡길이가 증가하고 M을 높이면 가져가는 떡길이가 감소하는 특성
# ===> 이때문에 이진탐색을 이용할 수 있는 것임
# 현재 이 높이로 자르면 조건 만족하는가? 에 대해 예/아니오로 답변 가능하므로 탐색 범위 좁혀서 또 질문

N,M=list(map(int, input().split()))
dducks = list(map(int, input().split()))

# 가능한 떡길이들 = 이진 탐색 위한 시작점과 끝점
start=0
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        # 자른 떡 양 계산
        # 잘린 떡의 크기가 클 경우에만 실제 떡 얻을 수 있으므로 이런 조건
        if x>mid:
            total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)
    if total < M:
        end = mid -1
    
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 탐색)
    else:
        result = mid
        start = mid+1

print(result)

# 정렬된 배열에서 특정 수의 개수 구하기
# 단, 이 문제의 시간 복잡도는 O(logN) 으로 설계하지 않으면 시간 초과
# 즉! 선형탐색으론 시간초과 판정. 데이터가 정렬되어 있으므로 이진탐색 수행하면 됨

# bisect_left, bisect_right 이용하면 됨