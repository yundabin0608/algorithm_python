# 제로

# 잘못된수를 부르면 0을 외쳐 쓴 수를 지움
# 모든 수를ㄹ 받아 적은 후 그 수의 합을 알아볼 것
# 첫줄 : K, 이후 K줄에 정수 1개씩 (0~1000000 정수값), 0이면 가장최근수 지우기
# 재민이가 치종적으로 적어낸 수 합 출력

from collections import deque

K=int(input())
stack=[]
for _ in range(K):
    temp=int(input())
    if temp==0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))