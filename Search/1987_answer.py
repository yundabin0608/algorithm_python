dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, alphabet_map[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < r) and (0 <= ny < c)) and (alphabet_map[nx][ny] not in ans):
                q.add((nx,ny,ans + alphabet_map[nx][ny]))
                answer = max(answer, len(ans)+1)



r,c = map(int, input().split())
alphabet_map=[]
for i in range(r):
    alphabet_map.append(list(input())) # 문자열이라 split 안해도 한글자씩 들어가짐   
answer = 1
BFS(0, 0)
print(answer)