def dfs(graph, start, visited):
    if start not in visited :
        print(start,end=' ')
        visited.add(start)
        for value in graph :
            dfs(graph, value, visited)

visited = set()
# 예제 그래프 (인접 리스트로 표현)
graph = {1:[2,5],
         2:[1,3,5],
         3:[2],
         4:[7],
         5:[1,2,6],
         6:[5],
         7:[4]
        }

dfs(graph, 1,visited)