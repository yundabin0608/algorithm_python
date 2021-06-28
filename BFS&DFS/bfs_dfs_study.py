def DFS(start_node):
    	# 1) stack 에 첫 번째 노드 넣으면서 시작
        stack = [start_node, ]
        
        while True:
            # 2) stack이 비어있는지 확인 
            if len(stack) == 0:
            	print('All node searched.')
                return None
                
            # 3) stack에서 맨 위의 노드를 pop
            node = stack.pop()
                
            # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
            if node == TARGET:
            	print('The target found.')
                return node
            
            # 5) node의 자식을 expand 해서 children에 저장
            children = expand(node)
            
            # 6) children을 stack에 쌓기
            stack.extend(children)
            
            # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복



# 이것이 파이썬 코테 웅앵웅
def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v]=True
  print(v,end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


from collections import deque
def bfs(graph, start, visited):
  # 시작 값으로 큐 초기화
  queue=deque([start])
  # 시작 노드 방문 처리
  visited[start]=True
  
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v=queue.popleft()
    print(v, end=' ')
    # 방문하지 않은 인접 노드들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True




