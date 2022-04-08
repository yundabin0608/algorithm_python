# 크게 만들기

# N자리수 주어질때 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수 구하는 프로그램 작성
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
number = input()
stack = []

# 4177252841에서 7앞 4와 1 사라지고 5앞의 2 8앞의 2가 사라지게 하는 코드
for i in range(N):
    while K>0 and stack and stack[-1] < number[i]:
            stack.pop()
            K -= 1
    stack.append(number[i])

# 9421의 경우 맨 뒤를 삭제해야 하므로 이런 경우를 위한 코드
stack = stack[:-K] if K else stack
print("".join(stack))
# print(*stack, sep="") 밑이 조금 더 느림

