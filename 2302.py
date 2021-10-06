# 극장 좌석

# 한줄로 된 좌석으로 왼쪽부터 1~N 이고 사람들은 자기좌석 좌우로 자리옮김이 가능
# 단 VIP 회원은 반드시 자기 자신의 좌석에 앉아야 하며 이동불가
# 1~N 까지 모든 좌석이 모두 팔렸고 VIP회원들의 좌석번호가 주어졌을때, 사람들이 서로 다른 좌석에 앉는 방법 가짓수

# N은 1이상 40이하 둘째줄은 고정석 개수 M (0~N사이) 

N=int(input())
M=int(input())

def fibo(n):
    curr, next = 0, 1
    for _ in range(n):
        curr, next = next, curr + next
    return curr

# VIP들이 앉는 좌석들 
fix_seat=[]
for _ in range(M):
    fix_seat.append(int(input())-1)

# VIP 앉는 자리 기준으로 쪼개지는 좌석들 넣음 VIP수+1개가 됨
slicing = []
index=0
for F in fix_seat:
    if index!=F:         # 같다면 VIP가 바로 옆에 존재
        slicing.append(F-index)
        index=F+1            #(=Fnum+1)
    else:
        index=F+1
if index!=N-1:
    slicing.append((N-1)-index)

# 슬라이싱된 녀석들 (좌석수)에 해당하는 경우의수들 곱하기
print(slicing)
answer=1
for s in slicing:
    tmp=fibo(s+1)
    answer=answer*tmp

print(answer)

