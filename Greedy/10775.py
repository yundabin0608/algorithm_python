# 공항
# 1~G를 번호로 갖는 게이트가 있는 공항
# 뱅기는 P개가 순서대로 도착할것이며 i번째 뱅기를 1번부터 gi(1~G)번째 게이트에 영구 도킹할것
# 뱅기가 어느 게이트에도 도킹 못하면 공항 폐쇠, 뱅기 도착 불가
# 뱅기 최대 도킹 개수

G = int(input())
P = int(input())
gate = []
answer=[]

# 자기가 해당하는 게이트중 가장 큰수에 넣도록 노력하는게 중요할듯

for i in range(P):
    gate.append(int(input()))
    answer.append(-1)

