# A와 B

# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꿀것
# 문자열 바꿀때 두가지 연산만 가능하며, S를 T로 바꿀수 있으면 1 없으면 0
# 문자열 뒤에 A 추가 혹은 문자열 뒤집고 B 추가

import sys
input = sys.stdin.readline

S = list(map(str, input().rstrip()))
T = list(map(str, input().rstrip()))

# 잘라나가기로 해보자
# 맨뒤가 A이면 A 없애고
# 맨뒤가 B이면 B빼고 반대로 뒤집기
#T길이가 S보다 기니까 T를 작게 만들어 나가기
while  len(T)!=len(S):
    if T[-1] == "A": T.pop()
    elif T[0] == "B":
        T.reverse()
        T.pop()

print(1 if S==T else 0)

