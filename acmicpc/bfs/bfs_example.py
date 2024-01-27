# 먼저 들어온 노드 순서대로 탐색하므로 queue사용
from collections import deque

def bfs(graph,start) :
    cnt = 0
    #방문할 노드들을 저장할 요소
    visted = set()
    #start요소를 초기값으로 갖는 queue생성
    queue = deque([start])
   
    #queue를 탐색하기 시작
    while queue :
        # 가장 처음에 들어온 값부터 확인 
        current_node = queue.popleft()
      
        # 현 코드가 아직 방문전 노드라면
        if current_node not in visted :
            #print(current_node,end=' ')
            visted.add(current_node)
            # 그래프에서 근접한 노드들을 탐색하기 시작한다.
            for neighbor in graph[current_node] :
                if neighbor not in visted:
                    queue.append(neighbor) 
                    cnt += 1
    
    print(cnt,len(visted))
                    



graph = {1:[2,5],
         2:[1,3,5],
         3:[2],
         4:[7],
         5:[1,2,6],
         6:[5],
         7:[4]
        }

bfs(graph,1)