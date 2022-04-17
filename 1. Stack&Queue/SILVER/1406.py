# 에디터

# 소문자만 편집 가능한 편집기로 최대 600,000 글자까지 입력 가능
# '커서'는 문장 맨앞, 맨뒤, 중간(연속된 두문자 사이)임의곳에 위치 가능
# 길이 L인 문자열이 현재 편집기에 있으면 커서 위치할 수 있는 곳은 L+1가지
# 명령어 L(커서 왼쪽 한칸 옮김),D(커서 오른쪽 한칸 옮김) 못옮기면 무시
# B(커서 왼쪽 문자 삭제),P$($문자 커서 왼쪽 추가)
# 모든 명령 수행 후 편집기에 입력되어있는 문자열 구하는 프로그램 수행

# wow.. 시간초과나서 다른답 본건데.. 난 이렇게 생각 못했음..
import sys
input = sys.stdin.readline

str = list(input())
stk = []
M = int(input())

for i in range(M):
    command = input().split()
    if command[0] == "L" and str:
        stk.append(str.pop())
    elif command[0] == "D" and stk:
        str.append(stk.pop())
    elif command[0] == "B" and str:
        str.pop()
    elif command[0] == "P":
        str.append(command[1])

print("".join(str + list(reversed(stk))))