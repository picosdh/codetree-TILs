import sys
sys.setrecursionlimit(10**6)

def dfs(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

# 입력 받기
N, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 스왑 정보 입력 및 그래프 구성
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = [0] * (N+1)

# 연결된 컴포넌트를 찾고 결과를 저장
for i in range(1, N+1):
    if not visited[i]:
        component = []
        dfs(i, graph, visited, component)
        size = len(component)
        for person in component:
            result[person] = size

# 결과 출력
for i in range(1, N+1):
    print(result[i])