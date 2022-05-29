# RGB 거리

# RGB 거리가 있으며 거리는 선분으로 나타내고 1번~N번집 존재
# 집은 R,G,B 중 한가지 색으로 칠하고 각 색마다 칠하는 비용이 다르다. 모든 집 칠하는 최소비용출력
# 1, 2번집은 색이 다르고, N, N-1 번집도 색이 다름
# i번집은 i-1, i+1 번집과 색 다를것 (i : 2~N-1)

import sys
input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    # 현재 값은 이전값(최소)+현재색으로 더해서 갱신함 (즉 맨 처음항 범위에서 빼야함)
    # 이전집은 나랑 다른색이어야 하므로 min에 같은 색 칠하는 비용은 제외
    colors[i][0] = min(colors[i-1][1], colors[i-1][2]) + colors[i][0]
    colors[i][1] = min(colors[i-1][0], colors[i-1][2]) + colors[i][1]
    colors[i][2] = min(colors[i-1][0], colors[i-1][1]) + colors[i][2]

print(min(colors[N-1]))