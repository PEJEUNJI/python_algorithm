import sys
loop = int(sys.stdin.readline().strip())
stack = []
for _ in range (loop) :
    target = sys.stdin.readline().strip()
    #1 X: 정수 X를 스택에 넣는다.
    if '1' in target :
        _,number = map(int,target.split())
        stack.append(number)
    #2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif target == '2' :
        print(stack.pop() if len(stack) > 0 else -1)
    #3: 스택에 들어있는 정수의 개수를 출력한다.
    elif target == '3' :
        print(len(stack))
    #4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif target == '4' :
        print(0 if len(stack) > 0 else 1)
    #5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif target == '5' :
        print(stack[-1] if len(stack) > 0 else -1)
        