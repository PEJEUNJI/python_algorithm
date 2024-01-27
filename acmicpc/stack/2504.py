
#)를 만나면 바로 앞의 값을 빼서 괄호를 확인하고 짝이 맞으면 맞는 값을 저장하고 있다가,
#다음 값이 open이면 지금까지 누적된 값을 하나씩 뺴면서 곱한 후 그 결과를 stack에 저장
#다 읽었으면 stack에 남아있는 값을 더한다.

import sys
input_line = sys.stdin.readline().strip()

stack = []



#닫는 괄호를 만났는데, input_data가 0 이 아니면, 다
result = 1
answer = 0
balanceFg = True
for index,ch in enumerate(input_line) :
    #() 쌍이 맞는지 확인
    if ch == ')' and len(stack) >0 and stack.pop() == '(' :
        #) 바로 앞의 값이 (인 경우 한쌍을 완성했으니 더한다. 
        if input_line[index-1] == '(' :
            answer += result
        #다음값 계산을 위해 2를 다시 나눠준다
        result //= 2
    #[]쌍이 맞는지 확인
    elif ch == ']' and len(stack) >0 and stack.pop() == '[' :
        #] 바로 앞의 값이 [인 경우 한쌍을 완성했으니 더한다. 
        if input_line[index-1] == '[' :
            answer += result
        result //= 3
    #)를 만나면 바로 앞의 값을 빼서 괄호를 확인하고 짝이 맞으면 맞는 값을 저장하고 있다가,
    elif ch == '(' :
        result *= 2
        stack.append(ch)
    elif ch =='[' :
        result *= 3
        stack.append(ch)
    #괄호가 맞지 않는 경우
    else :
         balanceFg =  False

if len(stack) > 0 : balanceFg =  False

        
if balanceFg : print(answer)
elif not balanceFg or len(stack) > 0  : print(0)