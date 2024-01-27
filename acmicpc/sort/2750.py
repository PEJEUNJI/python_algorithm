import sys
loop = int(input())
input_data = sorted([int(input()) for _ in range(loop)])
print(*input_data,sep='\n')
