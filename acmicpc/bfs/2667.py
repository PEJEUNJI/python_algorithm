#https://www.acmicpc.net/problem/2667
import sys
from collections import deque

size = int(sys.stdin.readline().strip())

graph = [[0]*size for _ in range(size)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
#붙어 있는 문자열 하나씩 자르면서 이차원 배열에 저장
for r in range(size) :
    line = sys.stdin.readline().strip()
    for c ,ch in enumerate(line) :
        graph[r][c] = int(ch)

count_list = []
def bfs(graph,r,c):
    queue = deque()
    queue.append((r,c))
    #이미 방문했음을 체크
    graph[r][c] = 0
     #근접한 노드중 접근가능한 합계를 구하기 위해 +1
    count = 1
    while queue:
        current_x, current_y = queue.popleft()
        #상하좌우 값 체크
        for index in range(4) :
            after_x = current_x + dx[index]
            after_y = current_y + dy[index]
            #근접한 노드 접근
            if 0<=after_x<size and 0<=after_y<size and graph[after_x][after_y] == 1 :
                queue.append((after_x,after_y))
                #근접한 노드중 접근가능한 합계를 구하기 위해 +1
                count += 1
                #이미 방문했음을 체크
                graph[after_x][after_y] = 0
    return count

total = 0            
for r in range(size) :
    for c in range(size) :
        #1이 나오는 순간 인접해 있는 모든 1을 탐색해야 함
        if graph[r][c] == 1 :
            #bfs가 호출된 횟수를 출력하기 위해서 
            total += 1
            count_list.append(bfs(graph,r,c))
           

print(total)
count_list.sort()
print(*count_list,sep='\n')