# 팰린드롬 만들기

# 동호는 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬 만듬
# 만들 수 있는 가장 짧은 팰린드롬의 길이 출력할 것

import sys
input = sys.stdin.readline

S = input().rstrip()
for i in range(len(S)):
    tmp = S[i:]
    if tmp == tmp[::-1]:
        print(len(S)+i)
        break

# 즉 펠린드롬이 아닌부분만큼만 뒤에 더 추가할것
# 펠린드롬인 부분은 0--- => -- 중앙 부분일것