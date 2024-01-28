import sys
from collections import deque

row, col = map(int,sys.stdin.readline().split())

graph = [[0]*col for _ in range(row)]

for r in range(row) :
    line = sys.stdin.readline().strip()
    for index, ch in enumerate (line) :
        graph[r][index] = int(ch)
#(0,1),(1,0),(0,-1),(-1,0)
#상하좌우값을 확인하며 좌표를 확인
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(graph,x,y) :
    queue = deque()
    queue.append((x,y))
     
    while queue :
        current_x, current_y = queue.popleft()
        #인접한 칸의 숫자를 체크
        for index in range(4):
            after_x = current_x + dx[index]
            after_y = current_y + dy[index]
            #갈수 있는 길이면 탐색 시작, 배열의 인덱스 체크 및 갈수 있는 길인지 체크
            if 0<=after_x<row and 0<=after_y< col and graph[after_x][after_y] == 1 :
                #가능한 길이면 지금까지 왔던 길의 갯수 +1
                graph[after_x][after_y] = graph[current_x][current_y] + 1
                queue.append((after_x,after_y))

#항상 첫칸은 이동가능한 1
bfs(graph,0,0) 
#가장 마지막 요소 출력
print(graph[row-1][col-1])