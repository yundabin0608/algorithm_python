import sys; 
sys.setrecursionlimit(100000)


r,c = map(int, input().split())
alphabet_map=[]
for i in range(r):
    alphabet_map.append(list(input())) # 문자열이라 split 안해도 한글자씩 들어가짐

dx=[1,-1,0,0]
dy=[0,0,1,-1]

alph=[]

def dfs(x,y):
    global answer

    alph.append(alphabet_map[y][x])

    for i in range(4):
        nx,ny= x+dx[i], y+dy[i]
        if 0<=nx<c and 0<=ny<r:
            target=alphabet_map[ny][nx]
            if target not in alph :
                answer=max(answer,len(alph)+1)
                dfs(nx,ny)

answer=1
dfs(0,0)

print(answer)
    


