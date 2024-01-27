    
#stack list를 이용해서 ( 는 저장, )가 입력되면 기존의 (를 꺼낸다.
loop = int(input())

def isValid(targetStr) :
    count = 0
    for ch in targetStr :
        if ch == '(' :
            count += 1
        elif count > 0 :
            count -= 1
        else :
            return 'NO'
    return 'NO' if count != 0  else 'YES'

for _ in range(loop) :
     print(isValid(input()))
