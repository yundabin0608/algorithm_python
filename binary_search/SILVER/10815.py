# 숫자카드
# 숫자카드 개수, 숫자카드에 적힌 정수 (-10,000,000~10,000,000), M, 상근이가 가진 숫자카드인지 아닌지 구해야할 M개의 정수
# 상근이는 숫자카드 N개 가졌고 정수 M개 주어졌을때 그게 상근이꺼인지 아닌지 구하기
# 상근이가 가지면 1 아니명 9

N=int(input())
have=list(map(int, input().split()))
M=int(input())
q = list(map(int, input().split()))

have.sort()

def binary_search(array, start, end, answer):
    
    while start <= end:
        mid = (start +end) // 2
        if 0 <= mid < N:
            if array[mid] < answer: 
                start = mid + 1
            else: 
                end = mid - 1
        else: break
    
    if 0 <= end + 1 < N:
        if array[end + 1] == answer: 
            print(1, end=" ")
        else: 
            print(0, end=" ")
    else: print(0, end=" ")
   
for i in range(M):
    binary_search(have, 0, N, i)

