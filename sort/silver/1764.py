# 듣보잡
# 듣도 못한 사람 명단, 보도 못한 사람명단 => 듣도 보도 못한 사람 명단 구하기
# 입력 : 듣도못한사람수 N, 보도 못한사람수 M, N줄 사람이름 후 M줄 사람이름
# 출력 :듣보잡의 수와 그 명단을 사전 순 출력 

# ==> 집합 set 이용했고 마지막에 answer에 정렬 sorted사용

N,M=map(int, input().split())
n_name = [] 
m_name = []

for _ in range(N):
    n_name.append(input())
for _ in range(M):
    m_name.append(input())

answer=[]
answer=set(n_name)&set(m_name)
print(len(answer))
for sort_answer in sorted(answer):
    print(sort_answer)
