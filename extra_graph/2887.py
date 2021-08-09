# 행성터널  => 최소신장트리 이용, 근데도 시간초과남 pyp3 하면 통과

# 왕국은 N개 행성, 행성은 3차원 좌표위 존재, A,B 연결시 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)
# 터널 N-1개 건설해서 모든 행성이 서로 연결때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

import sys

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        y=find_parent(parent[x])
        parent[x]=y
        return y

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b]=a

N=int(input())
parent=[i for i in range(N)]
planet_m=[]
edges=[]

for i in range(N):
    x,y,z=map(int, input().split())
    planet_m.append([x,y,z,i])

for i in range(3):
    planet_m.sort(key=lambda x:x[i])
    before = planet_m[0][3]
    for j in range(1,N):
        current=planet_m[j][3]
        edges.append([abs(planet_m[j][i]-planet_m[j-1][i]), before, current])
        before=current

edges.sort(key=lambda x:x[0])

cnt=0
answer=0
for dist, s, e in edges: # s,e => start, end
    if find_parent(s)!=find_parent(e):
        answer+=dist
        union_parent(s,e)
    if cnt==N-1:
        break

print(answer)