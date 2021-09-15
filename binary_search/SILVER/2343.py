# 기타레슨
# N: 강의 수, M: 블루레이수, 강의 순서 뒤바뀌지 말것

# 입력 : 1-> 강의 수 N (1 ≤ N ≤ 100,000) M (1 ≤ M ≤ N) 
# 다음 줄 -> 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어짐 (길이: 10,000분 이하)
# 출력 : 블루레이 크기중 최소


# 이분탐색을 해야하는데.. 블루레이수가 M보다 크면 크기를 줄이고 작으면 크기를 키우면서 조정
# (low, high, mid) 정해야하는데 low는 강의시간이 가장큰강의, high는 강의시간 총합

N,M=map(int,input().split())
lessons=list(map(int, input().split()))

low=max(lessons)
high=sum(lessons)
while low <= high:
    mid = (low + high) // 2   # 동영상들의 길이 합 체크할것
    cnt, temp = 0,0           # cnt => 블루레이수, temp => 블루레이 길이 누적
    for i in range(N):
        if temp + lessons[i] > mid:  # 반복문 돌면서 동영상길이 누적, mid보다 크면 블루레이 추가
            cnt += 1
            temp = 0
        temp += lessons[i]

    if temp : cnt+=1
    
    # 블루레이 수 작으면 mid 줄이기 => high 줄이기 & 블루레이 개수 크면 하나당 크기를 늘이기 => mid+1
    if cnt <= M: high = mid - 1  
    else: low = mid + 1          

print(low)