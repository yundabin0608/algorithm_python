# 앵무새

# 1앵무새 1문장 기억, 1문장은 여러 단어,이 단어들은 순서대로 말함
# 한 앵무새가 단어 말하고 다음 단어 말하기 전 간격동안 다른 앵무새가 가로채서 말하기 가능
# 앵무새가 단어 말하는 도중에는 가로채지 않으며 어떤 단어도 문장에 2번 이상 등장X
# A가 앵무새에게 전달한 문장들과 B가 받아적은 문장이 주어지고, 이문장이 규칙에 의해 나올수 있는지 판단


N=int(input()) # 앵무새 수

sentence = []
for _ in range(N):
    sentence.append(list(input().split()))

L = list(input().split())

answer = 1     # 1: possible 0: impossible

for word in L :
    flag = 0             # 1: pop 수행  0: pop 수행X           
    for i in range(N):  
        if len(sentence[i]) != 0 :
            if sentence[i][0] == word:
                sentence[i].pop(0)
                flag = 1
                break  
# L의 단어와 앵무새 문장의 첫번째 단어가 같으면 Si 에서 없에고 flag 바꾼후 break (담 단어로 넘기기)  
            
    if flag == 0 : answer = 0

# 앵무새들이 전달한 단어중 사용하지 않은 단어 있다면 impossible
for i in range(N):
    if sentence[i]: 
        print("Impossible")  
        exit() 
if answer == 1: print("Possible")
else :  print("Impossible")