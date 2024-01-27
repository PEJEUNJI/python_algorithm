import sys
from collections import deque

loop = int(sys.stdin.readline().strip())
dequeue = deque()

for _ in range(loop) :
    order = sys.stdin.readline().strip()
    #1 X: 정수 X를 덱의 앞에 넣는다.
    if len(order) > 1 :
        order, number = order.split()
        if order == '1' :
            dequeue.appendleft(number)
        #2 X: 정수 X를 덱의 뒤에 넣는다.
        elif order == '2' :
            dequeue.append(number)
    #3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.    
    elif order == '3' :
        print(dequeue.popleft() if len(dequeue) > 0 else -1)
    #4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif order == '4' :
        print(dequeue.pop() if len(dequeue) > 0 else -1)
    #5: 덱에 들어있는 정수의 개수를 출력한다.
    elif order == '5' :
        print(len(dequeue))
    #6: 덱이 비어있으면 1, 아니면 0을 출력한다.
    elif order == '6' :
        print(0 if len(dequeue) > 0 else 1)
    #7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif order == '7' :
        print(dequeue[0] if len(dequeue) > 0 else -1)
    #8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif order == '8' :
        print(dequeue[-1] if len(dequeue) > 0 else -1)