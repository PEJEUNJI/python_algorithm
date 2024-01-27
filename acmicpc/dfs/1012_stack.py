import sys
sys.setrecursionlimit(10**6)
from collections import deque

#(0,1),(1,0),(0,-1),(-1,0)
#상하좌우값을 확인하며 배추를 확인
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(graph, x, y) :
    #방문표시, 1인 경우만 호출하므로 방문 체크할 필요 없음
    graph[x][y] = 0
    # 해당 좌표의 상화좌우를 살피면서 배추가 있는지 확인
    for index in range(4) :
        after_x = x + dx[index]
        after_y = y + dy[index]
        #배열의 범위가 넘지 않는 범위에서 배추가 있는지 확인
        if after_x >= 0 and after_x < row and after_y >=0 and after_y < col and graph[after_x][after_y] == 1 :
            dfs(graph,after_x,after_y)

test_case = int(sys.stdin.readline().strip())

#test_case 만큼 test
for loop in range(test_case) :
    total = 0
    #해당 테스트 케이스의 조건을 구한다.
    #가로길이, 세로길이, 입력될 데이터의 수
    row,col,count = map(int,sys.stdin.readline().split())
    #그래프 초기화, row만큼 col열을 만든다
    graph = [[0]*col for _ in range(row)]
    for value in range(count) :
        #배추가 심어져 있는 좌표는 1로 변경
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    
    for x in range(row) :
        for y in range (col) :
            if graph[x][y] == 1 :
                dfs(graph,x,y)
                total += 1
    print(total)
        
