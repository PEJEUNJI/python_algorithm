import sys
from collections import deque

queue = deque()
loop = int(sys.stdin.readline().strip())
for _ in range (loop) :
    method = sys.stdin.readline().strip()
    #정수 X를 큐에 넣는 연산이다
    if 'push' in method:
        _,num = method.split()
        queue.append(int(num))
    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif method == 'pop' :
        print(queue.popleft() if queue else -1)
    # 큐에 들어있는 정수의 개수를 출력한다.
    elif method == 'size' : 
        print(len(queue))
    # 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif method == 'empty' :
        print(0 if len(queue)>0 else 1)
    # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif method == 'front' :
        print(queue[0] if queue else -1)
    # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif method == 'back' :
        print(queue[-1] if queue else -1)
