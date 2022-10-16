# A와 B2
# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꿀것
# 문자열 바꿀때 두가지 연산만 가능하며, S를 T로 바꿀수 있으면 1 없으면 0
# 문자열 뒤에 A 추가 혹은 문자열 뒤집고 B 추가

import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def dfs(string):
    if string == S : return True

    if len(string)>1 :
        if string[0]=="B" and dfs(string[1:][::-1]):
            return True
    
        if string[-1]=="A" and dfs(string[:-1]):
            return True
    
        return False

print(1 if dfs(T) else 0)