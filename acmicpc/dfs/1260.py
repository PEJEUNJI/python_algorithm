import sys
from collections import deque
vertex,edge,start = map(int,sys.stdin.readline().split())

graph = [[]*(vertex+1) for _ in range(vertex+1)]

for value in sys.stdin :
    nod1, nod2 = map(int,value.split())
    graph[nod1].append(nod2)
    graph[nod2].append(nod1)

#너비우선탐색 (queue)
def bfs(graph,start) :
    queue = deque([start])
    bfs_visited = set()

    while queue :
        current_index = queue.popleft()
        if current_index not in bfs_visited :
            print(current_index,end=' ')
            bfs_visited.add(current_index)
            for value in sorted(graph[current_index]) :
                if value not in bfs_visited :
                    queue.append(value)    

#깊이우선탐색 (stack)
def dfs(graph,node,visited):
    if node not in visited:
        print(node,end= ' ')
        visited.add(node)
        for value in sorted(graph[node]) :
            dfs(graph,value,visited)


dfs_visited = set()
dfs(graph,start,dfs_visited)
print()
bfs(graph,start)