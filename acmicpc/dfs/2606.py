import sys
computer_cnt = int(sys.stdin.readline().strip())
pair_cnt = int(sys.stdin.readline().strip())
# 이차원 배열
network = [[]*(computer_cnt +1) for _ in range(computer_cnt+1)]

for value in sys.stdin :
    nod1, nod2 = map(int,value.split())
    network[nod1].append(nod2)
    network[nod2].append(nod1)


def dfs(graph,start) :
    visited = set()
    stack = [start]

    while stack :
        #현재 노드를 구한다.
        current_node = stack.pop()
        #방문을 하기 전 노드이면 방문에 넣고 근접한 노드를 본다
        if current_node not in visited :
            visited.add(current_node)
            # 인접한 노드들 중 방문한적이 없는 노드는 stack넣는다
            for neighbor in graph[current_node] :
                if neighbor not in visited :
                    stack.append(neighbor)
    visited.discard(1)
    return len(visited)

print(dfs(network,1))

