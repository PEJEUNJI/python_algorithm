#https://www.acmicpc.net/problem/15650
import sys

scope, count = map(int,sys.stdin.readline().split())

result = []
def recur(start):
    if len(result) == count :
        print(*result,sep=' ')
    else :
        #오름차순으로만 되어야 하므로 start를 index+1로 변경해준다.
        for index in range (start,scope+1) :
            # 방문 여부 체크 후 
            if index not in result :
                result.append(index)
                recur(index+1)
                result.pop()      
recur(1)             

"""
import sys
from itertools import combinations

scope, count = map(int,sys.stdin.readline().split())
#scope 까지 숫자로 리스트를 생성 후 count를 넣고 combinations함수를 호출하면 count길이만큼 조합을 생성해준다
# (1,2) (2,1) 을 같은 값으로 간주한다.
result = combinations([index for index in range(1, scope+1)], count)

for list in result : 
    print(*list,sep=' ')
"""