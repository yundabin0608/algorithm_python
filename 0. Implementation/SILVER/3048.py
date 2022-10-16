# 개미

# 서로 반대로 이동하는 두 개미그룹이 길에서 만나면 1초에 한번씩 개미는 서로를 뛰어넘음
# 단 자신의 앞에 반대방향으로 움직이던 개미가 있는 경우 점프를 한다
# 예로 CBA><DEF 개미의 경우 1초 후(A와 D가 반대이므로) CBDAEF 
# 2초후 (B,D,A,E 가 반대이므로) CDBEAF
# T초후 개미 순서 구할것

import sys
input = sys.stdin.readline

N1, N2 = map(int,input().split())
ant1 = list(map(str,input().rstrip()))
ant2 = list(map(str,input().rstrip()))
ants = ant1[::-1] + ant2
T = int(input())

for t in range(T):
    if t>=len(ant1)+len(ant2)-1 : break

    for i in range(len(ants)-1):
        if ants[i] in ant1 and ants[i+1] in ant2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            if  ants[i+1] == ant1[0]: break

print(*ants, sep="")