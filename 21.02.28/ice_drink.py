n,m=map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

#DFS로 특정 노드를 방문한 뒤 연결된 모든 노드도 방문
def dfs(x,y):
    #주어진 범위 벗어나면 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    #현재 노드 방문X
    if graph[x][y]==0:
        graph[x][y]=1 #방문처리

        # 상,하,좌,우 위치 모두 재귀호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 위치에 대해 음료 채움
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:  #현 위치에서 DFS 수행
            result+=1
print(result)