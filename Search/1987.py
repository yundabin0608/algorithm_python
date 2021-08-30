# 알파벳

# 세로 R, 가로 C칸보드의 각 칸에는 대문자 알파벳이 하나씩 있고 1행1열에는 말이 있음
# 말은 상하좌우 이동가능하며 같은 알파벳이 적힌 칸을 두번 지날 수 없음

# 좌측상단(말이 위치한 칸)을 포함해 말이 지날 수 있는 최대 칸 수 출력
# bfs를 이용하면 이동 칸수 셀 때 count 이용 못함 => 알파벳맵 즉 지나온 알파벳들 세어주기

from collections import deque

r,c = map(int, input().split())
alphabet_map=[]
for i in range(r):
    alphabet_map.append(list(input())) # 문자열이라 split 안해도 한글자씩 들어가짐

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    count=1
    q=deque([])
    q.append([0,0])
    alph=[alphabet_map[0][0]]

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx,ny= x+dx[i], y+dy[i]
            if 0<=nx<c and 0<=ny<r:
                target=alphabet_map[ny][nx]
                if target not in alph :
                    alph.append(target)
                    q.append([nx, ny])
                    count=max(count, len(alph))
    return count

print(bfs())