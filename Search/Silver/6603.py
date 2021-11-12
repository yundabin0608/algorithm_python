# 로또

# {1, .... ,49} 에서 수 6개 고르기
# 49중 k(k>6)의 수를 골라 집합 s를 만든 후 그 수만 가지고 번호 선택
# 집합 s,k (6<k<13) 주어졌을때 수 고르는 모든 방법 구하는 프로그램 작성
# 각 줄이 k 집합으로 첫번째 수가 집합, 그뒤가 집합 k의 원소들, 마지막 입력시 0
# 출력은 각 테스트케이스마다 모든 방법 출력, 사전순, 테스트케이스마다 빈줄 한개씩


# 조합으로 풀것

from itertools import combinations
while True:
    # 각 테스트케이스를 받아서 0이면 멈추고 아니면 첫번째 숫자 떼고 그걸로 조합후 출력
    ins = input().split()
    if ins[0] == '0':
        break
    N=ins[0]
    ins = ins[1:]
    for i in combinations(ins, 6):
        print(" ".join(i))
    print()
