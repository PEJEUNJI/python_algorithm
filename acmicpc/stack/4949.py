import sys
     
append_target = ('(','[')
pop_target = (')',']')

     
def getResult(data):
    stack = []
    for ch in data :
        if ch in append_target :
            stack.append(ch) 
        elif ch in pop_target :
            pop_data = stack.pop() if len(stack) > 0 else 'no'
            if not((pop_data == '(' and ch == ')') or (pop_data == '[' and ch == ']')) :
                return 'no'
        
    return 'no' if len(stack) > 0 else 'yes'
            
     
#([ 만 추출. 순서대로 stack에 input, 닫는 괄호가 나오면 맞는 짝이 pop 결과로 나오는지 확인한다
for ch in sys.stdin:
   ch,_ = ch.split('\n')
   if ch == '.' : break
   else : print(getResult(ch))
     
    
