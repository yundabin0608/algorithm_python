array=[1,2,5,6,7]

# 1)선택정렬
# i는 가장 작은 데이터와 위치가 바뀐 인덱스를 의미 (가장 앞쪽 원소 위치)
for i in range(len(array)):
    min_index=i # 가장 작은 원소의 인덱스
    # 차례로 증가하며 선형탐색 수행
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]

# 2) 삽입정렬
for i in range(1, len(array)):
    for j in range(i, 0 ,-1): # 인덱스 i부터 1까지 1씩 감소하면서 반복
        if array[j]<array[j-1]: # 한칸씩 왼쪽으로 이동
              array[j], array[j-1]=array[j-1],array[j]
        # 자기보다 작은 데이터 만나면 그자리에서 멈춤
        else:
              break

# 3) 퀵 정렬
def quick_sort(array, start, end):
    # 원소가 하나면 종료
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end

    # left<=right의 경우 둘이 엇갈린것
    while(left<=right):
        # 피벗보다 큰 데이터 찾을때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        # 피벗보다 작은 데이터 찾을때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right-=1
        
        if(left>right): # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot]= array[pivot]=array[right]
        else:           # 앗갈리지 않았으면 작은데이터와 큰데이터 교체
            array[left], array[right]= array[right]=array[left]
    # 분할 후 양 덩어리에서 또 진행
    quick_sort(array,start,right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)

 # 퀵정렬 간결 ver
def quick_sort_(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:] # 슬라이싱으로 피벗을 제외한 리스트

    left_side =[x for x in tail if x <=pivot] # 분할된 왼쪽
    right_side=[x for x in tail if x>pivot]   # 분할된 오른쪽

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    return quick_sort_(left_side)+[pivot]+quick_sort_(right_side)

# 4) 계수정렬
# 모든 범위를 포함하는 리스트 선언하며 모든값은 0으로 초기화
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
 