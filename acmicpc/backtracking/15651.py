
import sys

scope, count = map(int,sys.stdin.readline().split())
result=[]
def recur(number) :
    if number == count :
        print(*result,sep=' ')
    else :
        #1~scope 까지 돌면서 리스트를 만든다
        #중복도 허용하므로 리스트에 값이 있는지 체크 하지 않는다
        for index in range(1,scope+1) :
            result.append(index)
            recur(number+1)
            result.pop()

recur(0)

"""
import sys
from itertools import product

scope, count = map(int,sys.stdin.readline().split())

result = product([value for value in range(1,scope+1)], repeat = count)
for list in result :
    print(*list,sep=' ')
"""