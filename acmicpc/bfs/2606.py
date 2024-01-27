import sys
from collections import deque
#컴퓨터의 수
computer_cnt = int(sys.stdin.readline().strip())
#한쌍의 수
pair_cnt = int(sys.stdin.readline().strip())
# 2차원 배열 생성 ,1~7까지 컴퓨터가 있으므로 1요소부터 7까지 담아야 함으로 +1
network = [[]*(computer_cnt+1) for _ in range(computer_cnt+1)]

# 인접한 요소를 모두 알아야 함으로 번갈아 가면서 저장
for value in sys.stdin :
    nod1, nod2 = map(int,value.split())
    network[nod1].append(nod2)
    network[nod2].append(nod1)

def bfs(network,start) :
    cnt = 0
    visted = set()
    queue  = deque([start])

    while queue :
        #현재요소
        current_node = queue.popleft()
        if current_node not in visted :
            #방문 했음을 체크 하기 위함
            visted.add(current_node)
            for neighbor in network[current_node] :
                # 아직 방문전 노드라면 접근을 위해서 queue에 넣는다
                if neighbor not in visted :
                    queue.append(neighbor)
    #노드 1은 빼야 한다
    visted.discard(1)                
    return len(visted)

print(bfs(network,1))