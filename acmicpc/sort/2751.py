import sys
input()
input_data = sorted([int(value) for value in sys.stdin])

print(*input_data,sep='\n')
