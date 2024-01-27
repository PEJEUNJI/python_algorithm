import sys
from collections import deque
length = int(sys.stdin.readline().strip())
status = sys.stdin.readline().split()
data = sys.stdin.readline().split()
loop = int(sys.stdin.readline().strip())
input_data = sys.stdin.readline().split()
result = deque()
#stack은 들어오자마자 pop해버리기에 어떤 값이 들어와도 그대로 queue까지 전달
#즉 결국 마지막 queue 원래 원소가 항상 return값이 된다.
 
for index,value in enumerate (data) :
    #queue인 경우만 result에 저장, appendleft로 앞에 추가해야 함
    if status[index] == '0' :
        result.appendleft(value)
#입력된 값들을 입력 기존 queue에 extend, loop 까지만 출력
#result.extend(input_data[0:loop-len(result)])
#print(*result,sep=" ")
result.extend(input_data)      
for i in range(loop):
  print(result.popleft(), end = " ")