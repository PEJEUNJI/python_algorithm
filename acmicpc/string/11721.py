import math
#열 개씩 끊어 출력하기
target = str(input())
#10개씩 출력
#for문을 len/10
loop = math.ceil(len(target) /10)
for i in range (loop) :
    print(target[i*10:(i*10)+10])