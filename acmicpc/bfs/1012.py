import sys
from collections import deque

#(0,1),(1,0),(0,-1),(-1,0)
#상하좌우값을 확인하며 배추를 확인
dx = [0,1,0,-1]
dy = [1,0,-1,0]

test_case = int(sys.stdin.readline().strip())

def bfs(graph, x,y) :
    queue = deque()
    #start값으로 초기화
    queue.append((x,y))
    graph[x][y] = 0
    while queue :
        #현재 좌표를 구한다
        current_x,current_y = queue.popleft()
        #상하좌우를 순회하면서 배추가 있는지 구한다.
        for index in range(4) :
            after_x = current_x + dx[index]
            after_y = current_y + dy[index]
            #배열의 범위를 벗어나지 않는 한에서 탐색해야함
            if after_x >=0 and after_y >= 0 and after_x < width and after_y < height :
                #배추가 심어 있는 좌표라면  탐색했으로 0 으로 변경해줘야 함.
                if graph[after_x][after_y] == 1:
                    #visited표시
                    graph[after_x][after_y] = 0
                    #다음 배추가 심어진 곳의 상하좌우를 살피기 위해 queue에 넣는다
                    queue.append((after_x,after_y))
                    

for index in range(test_case) :
    result = 0
    width,height,count = map(int,sys.stdin.readline().split())
    #세로 길이 만큼의 베열을 가로 길이만큼 생성, 반드시 세로*가로로 해야함
    #가로*세로로 해버리면 outindex에러 발생, (9,6) : 9번째 배열의 6번째 요소 접근이라는 의미
    graph = [[0]*height for _ in range(width)]
    
    #심어져 있는 배추의 좌표에 배추가 있다는 표시로 1을 저장한다.
    for _ in range(count) :
        x,y =  map(int,sys.stdin.readline().split())
        #그냥 예외처리 하는 방법 까먹지 않기 위해서 한번 해봄
        try :
            graph[x][y] = 1
        except Exception:
            print(x,y)

    for x in range(width) :
        for y in range(height) :
            #배추가 심어져 있다면, 근접한 배추들을 탐색하면서 0으로 변환 시작
            if graph[x][y] == 1 :
                bfs(graph,x,y)
                # 해당 배추들을 다 순회하고 난 뒤엔 count해준다.
                result += 1
    print(result)