# 나는 친구가 적다

# 교과서는 알파벳 소문자/대문자로만 이뤄져있으며 찾을 키워드도 마찬가지
# 잘못해서 키워드에 숫자가 들어갔음
# 이때 찾고싶어하는 키워드가 교과서에 있다면 1 아니면 0

import sys
input = sys.stdin.readline

S = input().rstrip()
K = input().rstrip()
LPS = [0 for _ in range(len(K))]

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

alphaS = [l for l in S if l.isalpha()]
answer =  KMP(alphaS, K)
print(1 if answer else 0)