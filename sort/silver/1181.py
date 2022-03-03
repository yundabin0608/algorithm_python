# 단어정렬

# 알파벳 소문자로 이뤄진 N개 단어가 들어오면 조건대로 정렬
# 길이가 짧은것 부터 길이 같으면 사전순

# 입력 : 첫줄 단어개수 N(1~20000) 둘째줄부터 단어주어짐 (50이내)
# 출력 : 조건에 따라 단어 출력. 같은단어 여러번입력 경우 한번씩만 출력

N=int(input())
words= []

for _ in range(N):
    words.append(input())

# 중복 제외 방법 => set로 변환하기 (중복 허락X) 이후 다시 리스트로 변환
words_s = set(words)
words = list(words_s)

# 알파벳 순 정렬 후 길이순 정렬 반대의 경우 다른 결과
words.sort() 
words.sort(key=len)

for i in words:
    print(words)

# 중복 제거해서 출력 => 오답이라 나옴
#for i in range(len(words)):
#    if words[i] != words[i-1]:
#        print(words[i])


