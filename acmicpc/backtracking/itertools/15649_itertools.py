import sys
from itertools import permutations

scope, count = map(int,sys.stdin.readline().split())

#수열 생성해주는 내장함수
result = permutations(range(1, scope +1), count)

for value in result :
    print(*value,sep=' ')