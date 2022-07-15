# 접미사 배열

# 접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬한 것
# 문자열 S가 주어졌을때, 모든 접미사를 사전순으로 정렬 후 출력할 것

import sys
input = sys.stdin.readline

S = input().rstrip()
answer = []
for i in range(len(S)):
    answer.append(S[i:])

for s in sorted(answer):
    print(s)