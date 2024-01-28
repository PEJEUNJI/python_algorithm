import sys
from collections import deque
vertex,edge,start = map(int,sys.stdin.readline().split())

graph = [[]*(vertex+1) for _ in range(vertex+1)]

for value in sys.stdin :
    nod1, nod2 = map(int,value.split())
    graph[nod1].append(nod2)
    graph[nod2].append(nod1)
#작은 점 부터 방문하므로 오름차순 정렬
for list in graph :
    list.sort()

#너비우선탐색 (queue)
def bfs(graph,start) :
    queue = deque([start])
    bfs_visited = set()

    while queue :
        #현재 노드를 추출
        current_index = queue.popleft()
        #현 노드가 방문전 노드이면 탐색시작
        if current_index not in bfs_visited :
            print(current_index,end=' ')
            #방문했으니 방문기록을 저장하고
            bfs_visited.add(current_index)
            #근접한 노드중 방문하지 않은 노드를 queue에 넣는다
            for value in graph[current_index] :
                if value not in bfs_visited :
                    queue.append(value)    

#깊이우선탐색 (stack)
def dfs(graph,node,visited):
    #방문전 노드이면
    if node not in visited:
        print(node,end= ' ')
        #방문노드에 저장하고
        visited.add(node)
        #근접노드를 탐색하기 위해 재호출
        for value in graph[node] :
            dfs(graph,value,visited)

dfs_visited = set()
dfs(graph,start,dfs_visited)

print()
bfs(graph,start)