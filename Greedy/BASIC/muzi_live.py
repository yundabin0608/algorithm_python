def solution(food_times, k):
    answer = 0
    size=len(food_times)
    total_time=0
    
    # 더 섭취할 음식이 없을땐 -1을 반환하므로
    for i in range(len(food_times)):
        total_time += food_times[i]
    if total_time <=k:
        return -1

    while(k>0):
        for time in range(size):
            if food_times[time]>0:
                food_times[time]-=1
                answer=time
                k-=1
    
            else:
                food_times[time]-=1
                answer=time
                
    
    #인덱스를 숫자번호로 변환
    index_change=answer+1 

    # 다시시작할때 먹었던거 다음것부터 먹어야함 마지막요소라면 맨 처음 음식을 가리켜야함
    if index_change==size:
        answer=1
        return answer
    else:
        answer+=index_change+1                       
        return answer

#몇개는 되고 몇개는 안됨          



