import sys
from itertools import product

scope, count = map(int,sys.stdin.readline().split())

result = product([value for value in range(1,scope+1)], repeat = count)
for list in result :
    print(*list,sep=' ')