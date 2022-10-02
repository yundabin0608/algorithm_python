# 부분문자열

# P가 S의 부분문자열인지 알아볼것, 각각 길이는 100만을 넘지 않음

import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()
LPS = [0 for x in range(len(P))]

def KMP(s, pattern):

    #LPS 배열만들기
    # LPS에 index -> index번까지 부분문자열에서 접두사=접미사인 길이
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = LPS[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            LPS[j] = i
    
    i = 0
    for j in range(len(s)):
        while i > 0 and s[j] != pattern[i]:
            i = LPS[i - 1]
        if s[j] == pattern[i]:
            if i == len(pattern)-1:
                return True
            else:
                i+=1
    return False

answer =  KMP(S, P)
print(1 if answer else 0)