#https://www.acmicpc.net/problem/15649
import sys
scope, count = map(int,sys.stdin.readline().split())

result = []
#for 을 동적으로 만들 수 없기에 재귀함수로 for문 횟수를 제어한다.(백트래킹)
def recur():
    #재귀 호출이 count만큼 만들어지면 중단하고 출력
    if len(result) == count :
        print(*result,sep=' ')
    else :
        #1부터 scope범위안의 수열을 구한다.
        for index in range(1,scope+1) :
            if index not in result :
                result.append(index)
                #한번 수행 했으므로 +1
                recur()
                #다음 index의 수열을 위해 가장 뒤의 값을 제거한다.
                #(1,2)->(1) ->(1,3)
                result.pop()

recur()

"""
import sys
from itertools import permutations

scope, count = map(int,sys.stdin.readline().split())

#수열 생성해주는 내장함수
result = permutations(range(1, scope +1), count)

for value in result :
    print(*value,sep=' ')
""" 