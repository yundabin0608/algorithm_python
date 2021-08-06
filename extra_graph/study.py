# 서로소 집합(disjoint Set) : 공통 원소가 없는 두 집합 = 합치기 찾기 자료구조 (Union Find)
# 서로소 집합 자료구조 - 서로소 부분 집합들로 나눠진 원소들의 데이터를 처리하기 위한 자료구조
# 서로소 집합 자료구조가 지원하는 두 연산 
# - 합집합 : 두개 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# - 찾기 : 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# => 합집합의 부모들을 동일하게 지정해주는걸 반복하면 됨 Ex) A(A') & B(B') B'를 A'으로 해줌
# 보통 더큰 루트노드가 더 작은 루트노드를 가리키는것이 관행이므로 이를 따르도록 함
# 서로소 집합 자료구조에선 연결성을 통해 쉽게 집합의 형태를 확인할 수 있음
# 단! 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없음 (부모테이블을 확인하며 재귀적으로 거슬러 올라가야함)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # x: 노드번호 
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기 => 당장 자신의 부모를 담고 있으며 루트와는 관련 없음을 의미
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# =================수행시간에서 단점이 있을 수 있음 (합집합 연산이 편향되게 이뤄지는 경우 찾기 함수가 비효율적임)==================

# 찾기 함수의 최적화 방법으로 경로압축 
# 찾기 함수를 재귀적으로 호출한 후 부모 테이블 값을 바로 갱신 ==> 부모의 값이 루트가 될 수 있도록 함

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#============================================================================================================
# 서로소 집합을 활용한 사이클 판별
# 서로소 집합은 무방향 그래프 내에서 사이클 판별할 때 사용 (방향그래프에서 사이클 여부는 DFS를 이용)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

#============================================================================================================
# 신장트리 : 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분그래프로 모든 노드가 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함
# 최소 신장 트리 : 최소의 비용으로 구성되는 신장트리 찾기
# 크쿠스칼 알고리즘 => 최소 신장 트리 알고리즘으로 그리디 알고리즘으로 분류됨
# 1. 간선 데이터를 비용에 따라 오름차순 정렬
# 2. 간선 하나씩 확인하며 현 간선이 사이클을 발생시키는지 확인하며 사이클이 발생하지 않는 경우 최소 신장트리에 포함시킴 이를 모든간선에 대해 반복

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b)) # 튜플을 이용하면 기본적으로 첫번째 원소를 기준으로 정렬함

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


#============================================================================================================
# 위상정렬 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것 => 큐와 DFS를 이용 가능
# 예로 선수과목을 고려한 학습 순서 설정

# 진입차수 : 특정한 노드로 들어오는 간선의 개수 Indegree
# 진출차수 : 특정 노드에서 나가는 간선의 개수  Outdegree

# 큐 이용시 진입차수가 0인 모든 노드를 큐에 넣고 큐가 빌때까지 다음을 반복
# 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거, 새롭게 진입차수가 0이 된 노드를 큐에 넣기
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재함 => 정렬 불가

from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()