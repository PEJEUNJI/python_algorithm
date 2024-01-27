from collections import deque 

loop,target = map(int,input().split())

queue = deque([value+1 for value in range(loop)])
result = []

while queue :
    for value in range(target-1):
        #target-1번 가장 왼쪽의 값을 제거하고 다시 queue 끝에 저장
        queue.append(queue.popleft())
    #target번째 요소가 가장 왼쪽에 위치함
    result.append(queue.popleft())
    
print('<',end='')
print(*result,sep=', ',end='')
print('>',end='')
