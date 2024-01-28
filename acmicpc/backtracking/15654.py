import sys

loop, length = map(int, sys.stdin.readline().split())
#사전 순으로 증가하는 순서로 출력해야 하므로 정렬
input_data = sorted(map(int, sys.stdin.readline().split()))

result = []
#for value in input_data, 방문여부 체크 해야 함
#len(result)가 length가 되면 출력
def recur():
    if len(result) == length :
        print(*result,sep=' ')
    else :
        for value in input_data :
            if value not in result :
                result.append(value)
                recur()
                result.pop()

recur()

"""
import sys
from itertools import permutations

loop, length = map(int, sys.stdin.readline().split())
#사전 순으로 증가하는 순서로 출력해야 하므로 정렬
input_data = sorted(map(int, sys.stdin.readline().split()))
result = permutations(input_data,length)

for list in result :
    print(*list,sep=' ')
"""