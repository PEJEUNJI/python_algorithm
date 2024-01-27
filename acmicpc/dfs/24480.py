import sys
sys.setrecursionlimit(10**6)

vertex, edge, start = map(int,sys.stdin.readline().split())

graph = [[]*(vertex+1) for _ in range(vertex+1)]
#순서를 저장하기 위한 리스트
answer = [0]*(vertex)

for value in sys.stdin :
    nod1, nod2 =  map(int,value.split())
    graph[nod1].append(nod2)
    graph[nod2].append(nod1)
#오름차순으로 정리
for list in graph :
    list.sort(reverse=True)

order = 1
def dfs(graph, start,answer):
    global order
    # 순서가 update전이므로 방문전
    if answer[start-1] == 0 :
        #순서를 구하는 문제임으로 order를 입력
        answer[start-1] = order
        order += 1
        #인접한 노드 체크
        for value in graph[start] :
            dfs(graph, value,answer)


dfs(graph, start ,answer)
print(*answer,sep='\n')

