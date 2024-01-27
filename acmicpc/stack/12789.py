# 리스트에 저장
# index와 같은 value가 있는지 먼저 체크 있으면 앞의 값들은 waitstack에 저장
# 더이상 없으면 waitstack에서 하나씩 빼면서 확인, 
import sys
from collections import deque
loop = int(sys.stdin.readline().strip())
# 5 4 1 3 2
input_data = deque(map(int,sys.stdin.readline().strip().split()))
#stack 자료구조로 해결하기 위해 순서를 전환
#input_data.reverse()

def checkResult(next_index):
    result = 'Nice'
    while next_index <= loop :  
        #다음 순서가 waiting 리스트에 있는경우
        if  next_index in waiting_stack :
            #바로 다음순서가 해당 번호가 맞는 경우 다음 순서로 update
            if waiting_stack.pop() == next_index :
                next_index +=1
            else :
                result =  'Sad'
                break
        #다음 순서가 처음 대기줄에 있는 경우
        elif next_index in input_data :
            #다시 waiting list를 재정렬 해야함
            next_index = moveWaiting(next_index)
    return result     

waiting_stack = []
#1부터 순서대로 있는지 확인
def moveWaiting(index) :
    while index in input_data:
        #데이터를 하나씩 이동
        value = input_data.popleft()
        # 다음값이 index값이 아니면 waiting stack에 누적
        if not index == value :
            waiting_stack.append(value)
        # 다음값이 index값이면 보내고, 다음 값을 찾는다
        else : 
            index += 1
    return index

index = moveWaiting(1)
if len(waiting_stack) > 0 or len(input_data) > 0 : print(checkResult(index))
else : print('Nice')