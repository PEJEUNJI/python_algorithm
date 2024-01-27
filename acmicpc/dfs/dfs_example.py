def dfs(graph, start):
    visited = set()  # 방문한 정점을 저장하기 위한 집합
    stack = [start]  # 스택을 이용하여 탐색 진행

    while stack:
        current_node = stack.pop()  # 스택에서 정점을 하나 꺼내옴
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)

            # 현재 정점과 인접한 정점들을 스택에 추가
            for neighbor in graph[current_node] :
                if neighbor not in visited:
                    stack.append(neighbor)

# 예제 그래프 (인접 리스트로 표현)
graph = {1:[2,5],
         2:[1,3,5],
         3:[2],
         4:[7],
         5:[1,2,6],
         6:[5],
         7:[4]
        }

dfs(graph, 1)