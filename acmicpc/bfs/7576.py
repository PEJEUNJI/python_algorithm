import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())

#입력값 저장
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(row)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

queue = deque()
#이미 익은 토마토는 queue 에 넣고 시작한다. 안그러면 중복 발생
#이미 익은 토마토를 다 넣고, 안 익은 토마토만 찾기 시작
for r in range(row) :
    for c in range (col) :
       if graph[r][c] == 1 :
           queue.append((r,c))


total_days = 0
def bfs(graph) :
    while queue:
        current_x, current_y = queue.popleft()
        for index in range(4) :
           after_x =  current_x + dx[index]
           after_y =  current_y + dy[index]
           # queue에 이미 익은 토마토만 있으므로 안익은 토마토만 찾아서 변경 시켜 준다
           if 0<=after_x<row and 0<=after_y<col and graph[after_x][after_y] == 0 :
                #당일에 변경한 토마토의 갯수를 구해야 하므로, 현재 탐색횟수 +1을 한다.
                #1부터 시작하므로 마지막 단계에서 -1 을 해줘야 함.
                graph[after_x][after_y] = graph[current_x][current_y] + 1
                queue.append((after_x,after_y))
   
bfs(graph)
max_value = 0
for r in range(row) :
    for c in range(col) :
        #모든 탐색을 다 했는데도 안익은 토마토가 있다면 모두 익지 못하는 상황
        if graph[r][c] == 0 : 
            print(-1)
            sys.exit()
        #최대값 찾기
        if(max_value < graph[r][c]) : 
            max_value = graph[r][c]

#처음 익은 토마토의 1은 빼줘야 하므로 
print(max_value-1)