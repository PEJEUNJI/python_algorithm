import sys
from collections import deque
loop = int(sys.stdin.readline().strip())
number_list = deque()
#추후 회전을 해도 최초 입력된 순서를 기억해야 하므로, index값도 함께 저장
for index,value in enumerate (sys.stdin.readline().split()) :
    number_list.append((int(value),index+1))

next_index = 0

for index in range(loop) :
    
    if not index == 0 :
        #index가 0보다 크면 index를 보지 않고 next_index 를 기준으로 양수이면 오른쪽으로 회전 
        if next_index > 0 :
            number_list.rotate(-1*(next_index-1))
            #대상값이 가장 왼쪽에 있으므로 popleft
            data = number_list.popleft()
        #next_index가 음수이면 오른쪽으로 회전
        else :
            number_list.rotate((next_index*-1)-1)
            #대상값이 가장 오른쪽에 있으므로 popleft
            data = number_list.pop()
    #맨 처음 요소이면 data = deque.popleft()
    else :
         data = number_list.popleft()        
    #data[0]인덱스값을 next_index에 저장후 data[1]번쨰 값, 즉 입력순서를 출력
    next_index = data[0]
    print(data[1],end=' ')