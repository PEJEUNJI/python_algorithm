import sys
from itertools import permutations

loop, length = map(int, sys.stdin.readline().split())
#사전 순으로 증가하는 순서로 출력해야 하므로 정렬
input_data = sorted(map(int, sys.stdin.readline().split()))
result = permutations(input_data,length)

for list in result :
    print(*list,sep=' ')