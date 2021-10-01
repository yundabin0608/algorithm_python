# N번째 큰 수

# N*N 표, 모든 수는 자신의 한 칸 위에 있는 수보다 큼
# 표가 주어졌을때 N번째로 큰 수를 찾는 프로그램 작성 (표에 채워진 수는 모두 다름)
# 굿노트에 풀이
# 한줄씩(N개 숫자)를 add로 받은 후 이전에 받았던거랑 합쳐서 큰순으로 정렬 
# 정렬한 후 N번째 큰수를 정하는것이므로 정렬한거를 N개까지만 짜름 (0~N개)
# 따라서 sort를 해도 최대 2N개만 하도록되는것!
# 우선순위 큐를 쓰기도 하던데 나는 정렬문제라서 정렬로 함

N=int(input())
matrix=[]

sort_matrix = list(map(int, input().split()))

for _ in range(N-1):
    add = list(map(int, input().split()))
    sort_matrix = sorted(sort_matrix+add, reverse=True)
    sort_matrix = sort_matrix[:N]

print(sort_matrix[N-1])

