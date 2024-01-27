
import sys
loop = int(sys.stdin.readline().strip())

input_data = list(map(int,sys.stdin.readline().split()))

#버블정렬
max = input_data[0]
min = input_data[0]
for index in range(1,loop) :
    if input_data[index] > max : max = input_data[index]
    elif input_data[index] < min : min = input_data[index]

print(min,max)

import sys

sys.stdin.readline()
list_data = list(map(int,sys.stdin.readline().split()))

print(min(list_data),max(list_data))