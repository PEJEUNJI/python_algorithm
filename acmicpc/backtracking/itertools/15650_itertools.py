import sys
from itertools import combinations

scope, count = map(int,sys.stdin.readline().split())
#scope 까지 숫자로 리스트를 생성 후 count를 넣고 combinations함수를 호출하면 count길이만큼 조합을 생성해준다
# (1,2) (2,1) 을 같은 값으로 간주한다.
result = combinations([index for index in range(1, scope+1)], count)

for list in result : 
    print(*list,sep=' ')
