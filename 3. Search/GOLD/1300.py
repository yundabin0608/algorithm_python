# K번째 수

# N*N 배열 A, 배열에 들어있는 수는 A[i][j] 이면 i*j
# 이를 일차원 배열에 넣으면 B의 크기는 N*N, 
# B오름차순 정렬시 B[k] 구하기
# A와 B의 인덱스는 1부터 시작

import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

# 임의의 수 mid가 몇번째 숫자인지 알아내는것. -> 이분탐색으로 어떤 수보다 작은 자연수의 곱이 몇개인지 찾을것.
# k보다 작은 수가 몇개인지 찾으면 k가 몇번째인지는 알 수 있음
# k번째 인덱스까지만 수를 알면 되고 여기엔 규칙있음 -> (k//행번호 ,N) 중에서 최소값이 개수임

# 처음엔 임의의 숫자니까 범위를 1~N*N 로 조사해야할것이라고 생각
# ?? back을 k로 하면 더 빨라지는데 왤까.. 왜지? N*N을 1*N으로 전개해보면 k번째 수들은 다 k보다 작음을 알 수 있음
answer, front, back = 1, 1, k
while(front<=back):
    mid = (front+back)//2

    tmp = 0 # mid보다 작거나 같은수의 개수
    for i in range(1,N+1):
        tmp += min(mid//i, N)

    if tmp>=k:
        answer = mid
        back = mid-1
    else:
        front = mid+1
print(answer)