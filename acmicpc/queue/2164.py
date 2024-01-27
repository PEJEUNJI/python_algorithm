import sys
from collections import deque

number = int(sys.stdin.readline().strip())

#순서대로 queue에 셋팅
queue = deque(i for i in range (1,number+1))

#popupleft()로 일단 하나를 버린뒤
#rotate(-1) 로 오른쪽으로 큐를 회전해서 가장 위의 값을 아래로 옮긴다.

while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())
    
print(*queue)
    
