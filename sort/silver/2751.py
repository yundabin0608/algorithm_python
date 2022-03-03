# 수 정렬하기 2 PyPy3_ver

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
# 입력 : 첫줄 입력개수 (1~1000000), 둘째줄부터 절대값 (0~1000000), 중복 없음
# 출력 : 첫줄부터 N개 줄에 오름차순으로 정렬한 결과 한줄 하나씩 출력

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

for n in numbers:
    print(n)